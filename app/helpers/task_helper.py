from app.tasks.task_processor import process_images

def initiate_image_processing(request_id, products):
    process_images.delay(request_id, products)  # Delays task execution to Celery worker
