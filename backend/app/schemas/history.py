from pydantic import BaseModel
from datetime import datetime


class HistoryResponse(BaseModel):
    id: int
    filename: str
    prediction: str
    confidence: float
    model: str
    created_at: datetime


    class Config:
        from_attributes = True