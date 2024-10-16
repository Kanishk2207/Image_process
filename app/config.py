import os
from dotenv import load_dotenv

load_dotenv()

class Settings():

    mongodb_uri = os.getenv("MONGODB_URI")
    redis_uri = os.getenv("REDIS_URI")

settings = Settings()