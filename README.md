# 🩺 AI Symptom Checker

An AI-powered web application that predicts possible diseases based on user-selected symptoms using Machine Learning and provides disease information, precautions, and risk assessment.

> **Disclaimer:** This project is for educational purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment.

## Live project Link:
  https://ai-symptom-checker-07uf.onrender.com
  
---

## 🚀 Features

- Predict possible diseases from symptoms
- Display top disease prediction
- Show disease description
- Recommend precautions
- Risk level assessment (Low/Medium/High)
- Simple and user-friendly interface
- FastAPI backend

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Machine Learning:** Scikit-learn (Random Forest)
- **Frontend:** HTML, CSS, JavaScript
- **Data Processing:** Pandas, NumPy
- **Model Storage:** Joblib
- **Deployment:** Render

---

## 📁 Project Structure

```text
AI-Symptom-Checker/
│
├── data/
├── models/
├── static/
├── templates/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

This project uses a Disease-Symptom dataset containing diseases and their associated symptoms for training the machine learning model.

---

## 🎯 Future Improvements

- AI-powered medical explanations
- Voice symptom input
- User authentication
- Prediction history
- Better UI/UX
- Multi-language support

---

## 🚀 How to Run the Project

1. Clone the Repository
git clone <your-github-repository-url>
cd AI-symptom-checker
2. Set Up the Backend

Create a Python virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Start the FastAPI backend:

uvicorn main:app --reload

The backend will run at:

http://127.0.0.1:8000

FastAPI API documentation is available at:

http://127.0.0.1:8000/docs
3. Run the Frontend

The frontend is built using HTML, CSS, and JavaScript.

If the frontend is served through FastAPI, open:

http://127.0.0.1:8000

If the frontend is maintained separately, open the frontend index.html file in a browser.

---

## 🤖 AI/ML Functionality

The application uses a **Random Forest Classifier** to predict a possible disease based on the symptoms selected by the user.

### Workflow

User Symptoms
        ↓
Symptom Preprocessing
        ↓
Feature Representation
        ↓
Random Forest Classifier
        ↓
Predicted Disease
        ↓
Disease Description & Precautions

### ML Components

- **Algorithm:** Random Forest Classifier
- **Data Processing:** Pandas, NumPy
- **Model Persistence:** Joblib
- **Training Data:** Disease-Symptom Dataset
- **Prediction:** Symptom-based disease classification

---

## 👩‍💻 Author

**Gauri**
