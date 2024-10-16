import uuid
from app.db.crud import create_image_request, get_image_status
from app.utils.file_utils import validate_csv
from app.helpers.task_helper import initiate_image_processing
from fastapi import HTTPException


async def fetch_status(request_id: str):
    status_data = await get_image_status(request_id)
    if not status_data:
        raise HTTPException(status_code=404, detail="Request ID not found")
    
    return {
        "request_id": request_id,
        "status": status_data.get("status"),
        "output_urls": status_data.get("output_urls", [])
    }

async def process_upload(file) -> str:
    df = validate_csv(file)
    request_id = str(uuid.uuid4())
    
    data = {
        "_id": request_id,
        "status": "Pending",
        "products": df.to_dict(orient="records")
    }
    
    await create_image_request(data)
    initiate_image_processing(request_id, data["products"])
    
    return request_id
