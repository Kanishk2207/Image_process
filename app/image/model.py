from pydantic import BaseModel
from typing import List, Optional

class StatusResponse(BaseModel):
    request_id: str
    status: str
    output_urls: Optional[List[str]] = []

class UploadResponse(BaseModel):
    request_id: str
    message: str
