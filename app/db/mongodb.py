import logging
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

class Database():
    client: AsyncIOMotorClient = None

db = Database()

async def db_connect():
    db.client = AsyncIOMotorClient(settings.mongodb_uri)
    print(f"Connected to db")

async def db_close():
    db.client.close()
    logging.info("Db connection closed")

def get_database():
    databse = db.client.get_database('dev_db')
    return databse

