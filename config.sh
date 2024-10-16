#!/bin/bash

IMAGE_NAME=image_processing
IMAGE_TAG=dev
DOCKER_FILE=$1
CONTAINER_NAME=image_processing_app
NETWORK=image-process
DIR=$(pwd)