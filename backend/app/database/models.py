from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from app.database.database import Base



class PredictionHistory(Base):

    __tablename__ = "prediction_history"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    filename = Column(
        String,
        nullable=False
    )


    prediction = Column(
        String,
        nullable=False
    )


    confidence = Column(
        Float,
        nullable=False
    )


    model = Column(
        String,
        nullable=False
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )