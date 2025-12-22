from fastapi import FastAPI
from app.api.predict_model_api import router as predict_router

app = FastAPI()
app.include_router(predict_router, prefix="/ml", tags=["ml"])