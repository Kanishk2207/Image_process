from celery import Celery
from app.config import settings

# celery_app = Celery(
#     'image_processor',
#     broker='redis://redis:6379/0',
#     backend='redis://redis:6379/0'
# )

celery_app = Celery(
    'image_processor',
    broker=settings.redis_uri,
    backend=settings.redis_uri
)


celery_app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json']
)
