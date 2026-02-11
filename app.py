import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("student_model_simple.pkl", "rb"))

st.title("🎓 Student Grade Prediction")

st.write("Enter student information:")

age = st.slider("Age", 15, 22, 18)
studytime = st.slider("Study Time (1–4)", 1, 4, 2)
failures = st.slider("Failures", 0, 3, 0)
absences = st.slider("Absences", 0, 50, 5)
g1 = st.slider("G1 Exam", 0, 20, 10)
g2 = st.slider("G2 Exam", 0, 20, 10)

if st.button("Predict Final Grade"):

    data = np.array([[age, studytime, failures, absences, g1, g2]])

    prediction = model.predict(data)

    st.success(f"Predicted G3 Grade: {prediction[0]:.2f}")
