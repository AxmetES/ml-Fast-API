from pathlib import Path
from typing import Any, Dict, List

import joblib
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
ARTIFACTS_DIR = BASE_DIR / "ml" / "artifacts"

MODEL_PATH = ARTIFACTS_DIR / "model.joblib"
META_PATH = ARTIFACTS_DIR / "meta.joblib"

model = joblib.load(MODEL_PATH)
meta = joblib.load(META_PATH)

THRESHOLD = float(meta.get("threshold", 0.35))
FEATURES: List[str] = meta.get("features") or []
FEATURES: List[str] = meta.get("features") or []
if not FEATURES and hasattr(model, "feature_names_in_"):
    FEATURES = list(model.feature_names_in_)

def _prepare_df(row: Dict[str, Any]) -> pd.DataFrame:
    X = pd.DataFrame([row])

    X = X.replace({pd.NA: np.nan, None: np.nan})

    cols = FEATURES or list(X.columns)

    for c in cols:
        if c not in X.columns:
            X[c] = np.nan

    X = X[cols]
    return X

def _risk_level(p: float) -> str:
    if p < 0.15:
        return "низкий"
    if p < THRESHOLD:
        return "средний"
    return "высокий"


def predict(row: Dict[str, Any]) -> Dict[str, Any]:
    X = _prepare_df(row)

    proba = float(model.predict_proba(X)[:, 1][0])
    pred = int(proba >= THRESHOLD)

    decision = "leave" if pred == 1 else "stay"
    decision_ru = "увольнение" if pred == 1 else "не увольнение"

    return {
        "probability_leave": f"{round(proba * 100, 2)} %",
        "decision": decision,
        "decision_ru": decision_ru,
        "risk_level": _risk_level(proba),
        "threshold": THRESHOLD,
    }
