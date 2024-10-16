from app.db.mongodb import get_database

async def get_image_collection():
    db = get_database()
    await db.create_collection('images', check_exists=False)

    image_collection = db.get_collection('images')

    return image_collection