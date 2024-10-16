# Image Processing System

This project is a scalable image processing system that accepts CSV files containing image URLs, compresses the images, and stores the processed images locally. The application is built with **FastAPI**, **Celery**, and **MongoDB**, using **Redis** for task management.

## Features

- Upload a CSV file with image URLs for processing.
- Asynchronous image processing using Celery.
- Optionally notify via a webhook when processing completes.
- Check the status of the processing job.
- Download processed results in CSV format.

## Tech Stack

- **Backend:** FastAPI
- **Asynchronous Tasks:** Celery with Redis
- **Database:** MongoDB
- **Containerization:** Docker

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose (optional, for easier setup)

### Clone the Repository

To start, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/image-processing-system.git
cd image-processing-system
```

## Configuration

The project requires a few configurations, which are defined in config.sh. You can adjust any of these configurations based on your needs.


```bash
#!/bin/bash

IMAGE_NAME=image_processing
IMAGE_TAG=dev
DOCKER_FILE=Dockerfile
CONTAINER_NAME=image_processing_app
NETWORK=image-process-net
DIR=$(pwd)

```

## Building the Docker Image

Run the build.sh script to build the Docker image:


```bash
./build.sh Dockerfile
```

## Running the Application
Use the run.sh script to start the application. This script will:

Check if MongoDB and Redis are running, and start them if necessary.
Run the FastAPI application and Celery worker within the same container.


```bash
./run_server.sh
```

## Accessing the Application
Once the application is running, you can access it at:

FastAPI API Docs: http://localhost:8000/docs

## API Endpoints
POST /api/upload: Upload a CSV file for processing.

GET /api/status/{request_id}: Check the status of a processing request.

GET /api/download/{request_id}: Download the processed results as a CSV file.