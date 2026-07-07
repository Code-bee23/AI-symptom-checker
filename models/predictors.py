from pathlib import Path
import joblib
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

# Load model and symptom list
model = joblib.load(BASE_DIR / "disease_model.pkl")
symptom_list = joblib.load(BASE_DIR / "symptom_list.pkl")


def predict_disease(selected_symptoms):

    # Create binary vector
    symptom_vector = np.zeros(len(symptom_list), dtype=int)

    for symptom in selected_symptoms:

        symptom = symptom.strip()

        if symptom in symptom_list:
            index = symptom_list.index(symptom)
            symptom_vector[index] = 1

    # Convert to DataFrame to match training features
    input_df = pd.DataFrame(
        [symptom_vector],
        columns=symptom_list
    )

    # Prediction
    disease = model.predict(input_df)[0]

    # Top predictions
    confidence = None
    top_predictions = []

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(input_df)[0]

        classes = model.classes_

        top_indices = probabilities.argsort()[-3:][::-1]

        confidence = round(probabilities[top_indices[0]] * 100, 2)

        for i in top_indices:
            top_predictions.append({
                "disease": classes[i],
                "probability": round(probabilities[i] * 100, 2)
            })

    return disease, confidence, top_predictions