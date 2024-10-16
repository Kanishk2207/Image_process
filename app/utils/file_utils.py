import pandas as pd
from fastapi import HTTPException

def validate_csv(file) -> pd.DataFrame:
    try:
        df = pd.read_csv(file)
        if not {"Serial Number", "Product Name", "Input Image Urls"}.issubset(df.columns):
            raise ValueError("CSV missing required columns.")
        return df
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
