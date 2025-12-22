from typing import Dict, Any

from pydantic import BaseModel


class PredictRequest(BaseModel):
    row: Dict[str, Any]

class PredictResponse(BaseModel):
    probability_leave: float
    decision: str
    decision_ru: str
    risk_level: str
    threshold: float