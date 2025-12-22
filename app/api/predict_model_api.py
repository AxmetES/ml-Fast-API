from fastapi import APIRouter
from app.schema.model_schema import PredictRequest
from app.service import pr_predict_service

router = APIRouter()

@router.post("/predict")
def predict(req: PredictRequest):
    return pr_predict_service.predict(req.row)

@router.get("/health")
def health_check():
    return {"status": "ok"}