from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import settings

from app.api import prediction
from app.api import report
from app.api import history

from app.database.database import Base, engine
from app.database import models

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.VERSION

)



app.include_router(
    prediction.router
)


app.include_router(
    report.router
)


app.include_router(
    history.router
)


app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs"
)



@app.get("/")

def home():

    return {

        "message":
        "Advanced AI Medical Intelligence Platform API"

    }



@app.get("/health")

def health_check():

    return {

        "status": "running"

    }