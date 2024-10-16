import requests
from PIL import Image
from io import BytesIO
import os
from app.db.crud import update_image_status
from app.tasks.celery_app import celery_app

@celery_app.task
def process_images(request_id, products):
    output_urls = []
    
    for product in products:
        input_urls = product['Input Image Urls'].split(',')
        compressed_urls = []

        for url in input_urls:
            response = requests.get(url.strip())
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                compressed_image = image.resize(
                    (image.width // 2, image.height // 2),
                    Image.ANTIALIAS
                )
                output_path = f"processed_images/{product['Product Name']}_{os.path.basename(url)}"
                compressed_image.save(output_path, optimize=True, quality=50)
                compressed_urls.append(output_path)

        output_urls.append({
            "Product Name": product['Product Name'],
            "Input Image Urls": product['Input Image Urls'],
            "Output Image Urls": ','.join(compressed_urls)
        })
    
    update_image_status(request_id, "Completed", output_urls)
    return output_urls