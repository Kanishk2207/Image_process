import csv
from fastapi import HTTPException
from io import StringIO
from app.db.crud import get_image_status

async def generate_csv(request_id: str) -> StringIO:
    status_data = await get_image_status(request_id)
    if not status_data:
        raise HTTPException(status_code=404, detail="Request ID not found")

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Serial Number", "Product Name", "Input Image Urls", "Output Image Urls"])
    
    for idx, product in enumerate(status_data.get("output_urls", []), start=1):
        writer.writerow([
            idx,
            product.get("Product Name", ""),
            product.get("Input Image Urls", ""),
            product.get("Output Image Urls", "")
        ])

    output.seek(0)
    return output
