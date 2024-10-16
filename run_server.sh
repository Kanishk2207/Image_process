#!/bin/bash
source config.sh

# Check if MongoDB container is running, start if not
if [ ! "$(docker ps -q -f name=mongodb)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=mongodb)" ]; then
        echo "Removing stopped MongoDB container..."
        docker rm mongodb
    fi
    echo "Starting MongoDB container..."
    docker run -d --name mongodb --network=$NETWORK -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=adminpass mongo
else
    echo "MongoDB is already running."
fi

# Check if Redis container is running, start if not
if [ ! "$(docker ps -q -f name=redis)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=redis)" ]; then
        echo "Removing stopped Redis container..."
        docker rm redis
    fi
    echo "Starting Redis container..."
    docker run -d --name redis --network=$NETWORK -p 6379:6379 redis
else
    echo "Redis is already running."
fi

# Check if the FastAPI and Celery container is running, stop and remove if it is
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing the existing container..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Check if the container exists but is not running
if [ "$(docker ps -aq -f status=exited -f name=$CONTAINER_NAME)" ]; then
    echo "Removing the existing stopped container..."
    docker rm $CONTAINER_NAME
fi

# Run the FastAPI and Celery app in a new container
docker run -it --network=$NETWORK -p 8000:8000 --restart always \
    --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_TAG bash -c "python3 main.py & celery -A app.tasks.celery_app.celery_app worker --loglevel=info"
