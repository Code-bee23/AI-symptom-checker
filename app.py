from pathlib import Path
import joblib
import pandas as pd

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.predictors import predict_disease

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"

# --------------------------------------------------
# FastAPI
# --------------------------------------------------

app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")

# --------------------------------------------------
# Load Model Files
# --------------------------------------------------

symptom_list = joblib.load(MODEL_DIR / "symptom_list.pkl")

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

description_df = pd.read_csv(DATA_DIR / "disease_description.csv")
precaution_df = pd.read_csv(DATA_DIR / "disease_precaution.csv")
severity_df = pd.read_csv(DATA_DIR / "symptom_severity.csv")

description_df.columns = description_df.columns.str.strip()
precaution_df.columns = precaution_df.columns.str.strip()
severity_df.columns = severity_df.columns.str.strip()

severity_df["Symptom"] = severity_df["Symptom"].str.strip()

# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "symptoms": symptom_list,
        },
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    selected_symptoms: list[str] = Form(...)
):

    selected_symptoms = [s.strip() for s in selected_symptoms]

    disease, confidence, top_predictions = predict_disease(selected_symptoms)

    # --------------------------------
    # Risk Score
    # --------------------------------

    risk_score = 0

    for symptom in selected_symptoms:

        row = severity_df[
            severity_df["Symptom"] == symptom
        ]

        if not row.empty:
            risk_score += int(row.iloc[0]["Symptom_severity"])

    if risk_score <= 5:
        risk = "🟢 Low"

    elif risk_score <= 12:
        risk = "🟡 Medium"

    else:
        risk = "🔴 High"

    # --------------------------------
    # Description
    # --------------------------------

    description = "Description not available."

    row = description_df[
        description_df["Disease"] == disease
    ]

    if not row.empty:
        description = row.iloc[0]["Symptom_Description"]

    # --------------------------------
    # Precautions
    # --------------------------------

    precautions = []

    row = precaution_df[
        precaution_df["Disease"] == disease
    ]

    if not row.empty:

        precautions = [
            row.iloc[0]["Symptom_precaution_0"],
            row.iloc[0]["Symptom_precaution_1"],
            row.iloc[0]["Symptom_precaution_2"],
            row.iloc[0]["Symptom_precaution_3"],
        ]

    # --------------------------------
    # AI Disclaimer
    # --------------------------------

    disclaimer = (
        "⚠️ This AI ccan provide information based on the symptoms you selected, but it "
        "should not be considered a medical diagnosis. "
        "Please consult a professional doctor, "
        "especially if symptoms are severe, persistent, or worsening."
    )

    # --------------------------------
    # Return Page
    # --------------------------------

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "prediction": disease,
            "risk": risk,
            "description": description,
            "precautions": precautions,
            "top_predictions": top_predictions,
            "selected_symptoms": selected_symptoms,
            "disclaimer": disclaimer
        }
    )
    