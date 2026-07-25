from fastapi import APIRouter

from app.schemas.report import (
    ReportRequest,
    ReportResponse
)

from app.services.llm_service import llm_service


router = APIRouter(
    prefix="/report",
    tags=["Medical Report"]
)


@router.post("/")
def generate_report(
    request: ReportRequest
):

    report = llm_service.generate_report(
        prediction=request.prediction,
        confidence=request.confidence
    )


    return ReportResponse(
        success=True,
        message="Medical report generated successfully.",
        medical_report=report
    )