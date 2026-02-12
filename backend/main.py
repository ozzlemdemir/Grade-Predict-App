from fastapi import FastAPI
import pickle
from flask import render_template
from flask import render_template
import numpy as np

app = FastAPI()

# Model yükle
model = pickle.load(open("student_model_simple.pkl", "rb"))

@app.get("/")
def root():
    return {"message": "Student Prediction API is running 🚀"}

@app.post("/predict")
def predict(
    age: int,
    studytime: int,
    failures: int,
    absences: int,
    g1: int,
    g2: int
):
    
    data = np.array([[age, studytime, failures, absences, g1, g2]])
    
    prediction = model.predict(data)
    
    return {
        "predicted_G3": float(prediction[0])
    }

    return render_template("html/index.html", prediction_text=f"Predicted G3 Grade: {prediction[0]:.2f}")