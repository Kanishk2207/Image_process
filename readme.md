Image Processing System
This project is a scalable image processing system that accepts CSV files containing image URLs, compresses the images, and stores the processed images locally. The application is built with FastAPI, Celery, and MongoDB, using Redis for task management.

Features
Upload a CSV file with image URLs for processing.
Asynchronous image processing using Celery.
Optionally notify via a webhook when processing completes.
Check the status of the processing job.
Download processed results in CSV format.
Tech Stack
Backend: FastAPI
Asynchronous Tasks: Celery with Redis
Database: MongoDB
Containerization: Docker
Setup Instructions
Prerequisites
Docker
Docker Compose (optional, for easier setup)
Clone the Repository
To start, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/image-processing-system.git
cd image-processing-system
Configuration
The project requires a few configurations, which are defined in config.sh. You can adjust any of these configurations based on your needs.

config.sh
bash
Copy code
#!/bin/bash

IMAGE_NAME=image_processing
IMAGE_TAG=dev
DOCKER_FILE=Dockerfile
CONTAINER_NAME=image_processing_app
NETWORK=image-process-net
DIR=$(pwd)
Building the Docker Image
Run the build.sh script to build the Docker image:

bash
Copy code
./build.sh Dockerfile
Running the Application
Use the run.sh script to start the application. This script will:

Check if MongoDB and Redis are running, and start them if necessary.
Run the FastAPI application and Celery worker within the same container.
bash
Copy code
./run_server.sh
Accessing the Application
Once the application is running, you can access it at:

FastAPI API Docs: http://localhost:8000/docs
API Endpoints
POST /api/upload: Upload a CSV file for processing.
GET /api/status/{request_id}: Check the status of a processing request.
GET /api/download/{request_id}: Download the processed results as a CSV file.
Example Usage
Upload a CSV file:

bash
Copy code
curl -X 'POST' \
  'http://localhost:8000/api/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path/to/yourfile.csv' \
  -F 'webhook_url=http://your-webhook-url.com'
Check the Status:

bash
Copy code
curl -X 'GET' 'http://localhost:8000/api/status/{request_id}' -H 'accept: application/json'
Download Processed Data:

bash
Copy code
curl -O 'http://localhost:8000/api/download/{request_id}'
Stopping the Application
To stop the application and remove containers, run:

bash
Copy code
docker stop mongodb redis $CONTAINER_NAME
docker rm mongodb redis $CONTAINER_NAME
Troubleshooting
If you encounter issues with Docker, ensure that your Docker daemon is running and that you have the necessary permissions to execute Docker commands.

Contributing
Feel free to submit issues and pull requests! Contributions are always welcome.

