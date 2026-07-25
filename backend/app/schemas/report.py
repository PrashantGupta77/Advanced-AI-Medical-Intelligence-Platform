from pydantic import BaseModel


class ReportRequest(BaseModel):
    prediction: str
    confidence: float


class ReportResponse(BaseModel):
    success: bool
    message: str
    medical_report: str