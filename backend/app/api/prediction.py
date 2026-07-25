import os
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from app.services.model_service import model_service
from app.services.gradcam_service import gradcam_service

from app.schemas.prediction import (
    PredictionResponse,
    PredictionData
)

from app.database.database import get_db
from app.database.models import PredictionHistory

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@router.post(
    "/",
    response_model=PredictionResponse
)
async def predict_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a valid image."
        )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    try:

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        result = model_service.predict(
            file_path
        )

        gradcam_path = gradcam_service.generate_gradcam(
            file_path
        )


        # Save prediction history to the database
        prediction_history = PredictionHistory(
            filename=file.filename,
            prediction=result["prediction"],
            confidence=result["confidence"],
            model=result["model"]
        )
        db.add(prediction_history)
        db.commit()
        db.refresh(prediction_history)

        return PredictionResponse(
            success=True,
            message="Prediction completed successfully.",
            data=PredictionData(
                id=prediction_history.id,
                filename=file.filename,
                prediction=result["prediction"],
                confidence=result["confidence"],
                model=result["model"],
                gradcam_image=gradcam_path,
            )
        )

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)