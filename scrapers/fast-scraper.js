import { CheerioCrawler, Dataset } from 'crawlee';
import fs from 'fs';
import parse from 'csv-parse';

// Function to parse CSV into JSON
const parseCSV = async (filePath) => {
    return new Promise((resolve, reject) => {
        const records = [];
        fs.createReadStream(filePath)
            .pipe(parse({ columns: true }))
            .on('data', (data) => records.push(data))
            .on('end', () => resolve(records))
            .on('error', (error) => reject(error));
    });
};

// Function to check `robots.txt`
const canScrape = async (url) => {
    try {
        const robotsUrl = new URL('/robots.txt', url).href;
        const response = await fetch(robotsUrl);
        if (!response.ok) {
            console.warn(`Could not fetch robots.txt for ${url}. Defaulting to allow.`);
            return true; // Default to allow if robots.txt is not reachable
        }
        const robotsText = await response.text();
        return !robotsText.includes('Disallow: /'); // Check for broad disallow
    } catch (err) {
        console.error(`Error checking robots.txt for ${url}: ${err.message}`);
        return false;
    }
};

// Main scraper function
const scrapeDocs = async () => {
    // Load API URLs from CSV
    const apis = await parseCSV('./api_urls.csv');
    console.log(`Loaded ${apis.length} API URLs.`);

    const crawler = new CheerioCrawler({
        async requestHandler({ request, $, log }) {
            // Extract relevant content
            const title = $('title').text();
            const content = $('body').text().trim();

            // Save scraped data to a dataset
            await Dataset.pushData({
                apiName: request.userData.apiName,
                url: request.url,
                title,
                content,
            });

            log.info(`Scraped: ${request.url}`);
        },
        failedRequestHandler({ request, error }) {
            console.error(`Failed to scrape ${request.url}: ${error.message}`);
        },
    });

    // Check `robots.txt` and enqueue URLs
    for (const api of apis) {
        const { API_Name, Official_Documentation_URL } = api;
        if (await canScrape(Official_Documentation_URL)) {
            crawler.addRequests([
                {
                    url: Official_Documentation_URL,
                    userData: { apiName: API_Name },
                },
            ]);
        } else {
            console.warn(`Skipping ${Official_Documentation_URL}: Not allowed by robots.txt`);
        }
    }

    // Run the crawler
    await crawler.run();
};

// Run the scraper
scrapeDocs().then(() => {
    console.log('Scraping completed. Dataset saved.');
});
