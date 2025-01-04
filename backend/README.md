
## Backend Features

- API Metadata Retrieval: Return details like endpoints, methods, and parameters
- Categorized Browsing: Return pre-categorized API lists
- Subscription Management: Allow users to subscribe to API updates
- Notifications: Send updates to users via email or webhooks (later)

## Backend File Structure

```plaintext
backend/
│
├── app.py                # Main application file
├── config.py             # Configuration settings (e.g., database URI)
├── requirements.txt      # Dependencies
├── Dockerfile            # Dockerfile for containerizing the backend
├── routes/
│   ├── __init__.py       # Route initialization
│   ├── api_routes.py     # Routes for API search and metadata
│   ├── user_routes.py    # Routes for user subscriptions and notifications
│
├── models/
│   ├── __init__.py       # Model initialization
│   ├── api_model.py      # MongoDB schema for API metadata
│   ├── user_model.py     # MongoDB schema for users and subscriptions
│
└── utils/
    ├── scraper.py        # Utility to scrape and fetch API data
    ├── notifier.py       # Utility to send notifications
    └── helpers.py        # Helper functions

```

## Backend Setup

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Backend and Database

```bash
docker-compose up --build
```

### Check MongoDB Entries

Enter the MongoDB shell through docker:
```bash
docker exec -it updapi-mongodb mongo
use updapi
```

View DB:
```bash
db.apis.find().pretty()
```

### Test endpoints

- API Search: Search APIs by name, category, or functionality.

```bash
GET http://localhost:5000/api/search?query=Stripe
```

Get categories
```bash
GET http://localhost:5000/api/categories
```

Subscribe to an API
```bash
POST http://localhost:5000/user/subscribe
Body: { "email": "test@example.com", "api_name": "Stripe" }
```

TODO:
- Rate Limiting: Add a rate limiter for free user
- Authentication: Implement OAuth or JWT for user accounts
- Scraper Integration: Automate API metadata fetching using tools like Crawlee