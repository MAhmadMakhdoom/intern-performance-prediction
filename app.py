
import streamlit as st
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("🎯 Intern Performance Predictor")
st.write("Enter intern details to predict performance score.")

completion_time = st.slider("Task Completion Time (days)", 1.0, 7.0, 3.5)
feedback_rating = st.slider("Feedback Rating", 1.0, 5.0, 3.0)
attendance      = st.slider("Attendance %", 0.0, 100.0, 75.0)

if st.button("Predict Performance Score"):
    input_data   = np.array([[completion_time, feedback_rating, attendance]])
    input_scaled = scaler.transform(input_data)
    prediction   = model.predict(input_scaled)[0]

    if prediction >= 75:
        st.success(f"✅ Score: {prediction:.2f} — Likely to EXCEL!")
    elif prediction >= 50:
        st.warning(f"⚠️ Score: {prediction:.2f} — Average Performer")
    else:
        st.error(f"❌ Score: {prediction:.2f} — Likely to STRUGGLE")
