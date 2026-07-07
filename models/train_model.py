from pathlib import Path
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ------------------------------------
# Paths
# ------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

# ------------------------------------
# Load Dataset
# ------------------------------------

train_df = pd.read_csv(DATA_DIR / "Training.csv")
test_df = pd.read_csv(DATA_DIR / "Testing.csv")

print("Training Shape :", train_df.shape)
print("Testing Shape  :", test_df.shape)

# Remove duplicate rows
train_df = train_df.drop_duplicates()
test_df = test_df.drop_duplicates()

print("\nAfter removing duplicates")
print("Training Shape :", train_df.shape)
print("Testing Shape  :", test_df.shape)

# ------------------------------------
# Features & Labels
# ------------------------------------

X_train = train_df.iloc[:, :-1]
y_train = train_df.iloc[:, -1]

X_test = test_df.iloc[:, :-1]
y_test = test_df.iloc[:, -1]

# Save feature names
symptom_list = list(X_train.columns)

# ------------------------------------
# Train Model
# ------------------------------------

print("\nTraining Random Forest...")

model = RandomForestClassifier(
    n_estimators=500,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ------------------------------------
# Evaluation
# ------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n" + "=" * 50)
print("Accuracy :", round(accuracy * 100, 2), "%")
print("=" * 50)

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, predictions))

# ------------------------------------
# Save Model
# ------------------------------------

joblib.dump(model, BASE_DIR / "disease_model.pkl")
joblib.dump(symptom_list, BASE_DIR / "symptom_list.pkl")

print("\n✅ disease_model.pkl saved")
print("✅ symptom_list.pkl saved")