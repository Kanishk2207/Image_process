import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from app.db.mongodb import db_connect, db_close, get_database
from app.image.views import router as image_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_connect()
    db = get_database()
    await db.create_collection('test1', check_exists=False)
    yield
    await db_close()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {"message": f"The app is healthy"}

app.include_router(image_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        reload=True
        )