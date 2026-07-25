from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.database.models import PredictionHistory

from app.schemas.history import HistoryResponse



router = APIRouter(

    prefix="/history",

    tags=["Prediction History"]

)



@router.get("/", response_model=list[HistoryResponse])
def get_history(

    db: Session = Depends(get_db)

):


    records = db.query(
        PredictionHistory
    ).order_by(
        PredictionHistory.id.desc()
    ).all()


    return records