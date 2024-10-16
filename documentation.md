a. FastAPI App
/upload Endpoint: Accepts a CSV file, initiates the image processing request, and returns a unique request ID.
/status Endpoint: Allows users to check the processing status by providing the request ID.
/download Endpoint: Enables users to download the output CSV file once processing is complete.
b. Database (MongoDB)
Stores image processing requests with the fields:
request_id: Unique identifier for each request.
status: Current status of processing (e.g., Pending, Completed).
products: List of products with image URLs.
output_urls: List of processed image URLs.
webhook_url: Optional URL for notifying users when processing completes.
c. Celery Task Queue
Manages asynchronous processing tasks. When an image processing request is submitted, Celery queues the task for processing without blocking the FastAPI app.
d. Celery Worker
Task Processor: Fetches images from URLs, compresses them, saves them locally, updates the database, and triggers a webhook if specified.
e. Helpers
CSV Helper: Generates CSV files based on processed data.
File Utils: Validates and parses CSV files during upload.
Task Helper: Manages interaction with Celery tasks.
3. Database Schema
Here’s the schema design for MongoDB, structured to store data for each request:

json
Copy code
{
    "_id": "string (request_id)",
    "status": "string (Pending, Processing, Completed)",
    "products": [
        {
            "Product Name": "string",
            "Input Image Urls": "string (comma-separated URLs)",
            "Output Image Urls": "string (comma-separated processed URLs)"
        }
    ],
    "output_urls": [
        {
            "Product Name": "string",
            "Input Image Urls": "string (comma-separated URLs)",
            "Output Image Urls": "string (comma-separated processed URLs)"
        }
    ],
    "webhook_url": "string (optional)"
}
_id: Unique identifier (UUID) for each request.
status: Tracks the status of the processing request.
products: Contains the raw data from the CSV file.
output_urls: Populated after processing with URLs of the processed images.
