from app.db.mongodb_utils import get_image_collection

async def create_image_request(data: dict):
    collection = await get_image_collection()
    result = await collection.insert_one(data)
    return str(result.inserted_id)

async def update_image_status(request_id: str, status: str, output_urls=None):
    collection = await get_image_collection()
    update_data = {"status": status}
    if output_urls:
        update_data["output_urls"] = output_urls
    await collection.update_one({"_id": request_id}, {"$set": update_data})

async def get_image_status(request_id: str):
    collection = await get_image_collection()
    result = await collection.find_one({"_id": request_id}, {"_id": 0, "status": 1, "output_urls": 1})
    return result
