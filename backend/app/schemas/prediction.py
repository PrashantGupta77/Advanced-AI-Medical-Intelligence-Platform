from pydantic import BaseModel


class PredictionData(BaseModel):
    id: int
    filename: str
    prediction: str
    confidence: float
    model: str
    gradcam_image: str


class PredictionResponse(BaseModel):
    success: bool
    message: str
    data: PredictionData