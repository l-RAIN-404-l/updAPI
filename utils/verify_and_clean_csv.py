import csv
import requests
import os

## Function to check if a URL is broken
## Returns True if URL was not found (404 status code) or if an error occurred
def is_broken_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, timeout=5, allow_redirects=True, headers=headers)
        return response.status_code == 404
    except requests.exceptions.RequestException as e:
        return True


def verify_csv(file_path):
    cleaned_rows = []
    invalid_urls = 0
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        cleaned_rows.append(header)
        for row in csv_reader:
            api_name = row[0]
            urls = row[1:]
            cleaned_row = [api_name]
            for url in urls:
                if is_broken_url(url):
                    print(f"URL for {api_name} is invalid: {url}")
                else:
                    cleaned_row.append(url)
            if len(cleaned_row) > 1:
                cleaned_rows.append(cleaned_row)
    return cleaned_rows, invalid_urls

def clean_csv(file_path, cleaned_rows):
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for row in cleaned_rows:
            csv_writer.writerow(row)
    print(f"Cleaned CSV saved to: {file_path}")


if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)

    # Construct the path to the file in the parent directory
    parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
    csv_file_path = os.path.join(parent_dir, 'api-docs-urls.csv')
    print(f"Beginning verification of the CSV file: {csv_file_path}")
    cleaned_rows, invalid_urls = verify_csv(csv_file_path)
    print(f"Verification complete.")
    print(f"Beginning cleaning of the CSV file: {csv_file_path}")
    clean_csv(csv_file_path, cleaned_rows)
    print(f"Cleaned {invalid_urls} invalid URLs from the CSV file.")
    