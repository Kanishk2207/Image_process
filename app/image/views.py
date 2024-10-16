from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from app.image.service import process_upload, fetch_status
from app.image.model import UploadResponse, StatusResponse
from app.helpers.csv_helper import generate_csv


router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
async def upload_csv(file: UploadFile):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="File must be a CSV")
    
    request_id = await process_upload(file.file)
    return {"request_id": request_id, "message": "File uploaded successfully"}

@router.get("/status/{request_id}", response_model=StatusResponse)
async def get_status(request_id: str):
    return await fetch_status(request_id)

@router.get("/download/{request_id}")
async def download_csv(request_id: str):
    csv_file = await generate_csv(request_id)
    response = StreamingResponse(
        iter([csv_file.getvalue()]),
        media_type="text/csv"
    )
    response.headers["Content-Disposition"] = f"attachment; filename=output_{request_id}.csv"
    return response
