import { MongoClient } from 'mongodb';
import { CheerioCrawler } from 'crawlee';

const MONGO_URI = 'mongodb://localhost:27017'; // Replace with your MongoDB URI
const DATABASE_NAME = 'updapi';               // Replace with your database name

async function connectToDb() {
    const client = new MongoClient(MONGO_URI);
    await client.connect();
    console.log('Connected to MongoDB');
    return client.db(DATABASE_NAME);
}

(async () => {
    const db = await connectToDb();

    const crawler = new CheerioCrawler({
        requestHandler,
        requestQueue: await CheerioCrawler.openRequestQueue(null, { persistRequests: false }),
        keyValueStore: null, // Prevents creating a key-value store
        dataset: null,      // Prevents creating a dataset
    });
    

    // Start the crawler
    await crawler.run(['https://stripe.com/docs/api']);
})();

