import streamlit as st
import numpy as np
import joblib

model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Heart Disease Prediction")
age = st.number_input("Age",1,100)
sex = st.selectbox("Sex",[0,1])
cp = st.selectbox("Chest Pain Type",[0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholestrol")
fbs = st.selectbox("Fasting Blood Sugar",[0,1])
restecg = st.selectbox("Rest ECG",[0,1,2])
thalach = st.number_input("Maximum Heart Rate")
exang = st.selectbox("Exercise Induced Angina",[0,1])
oldpeak = st.number_input("Old Peak")
slope = st.selectbox("Slope",[0,1,2])
ca = st.selectbox("Major Vessels",[0,1,2,3])
thal = st.selectbox("Thal",[0,1,2,3])

if st.button("Predict"):
    data = np.array([[
        age,sex,cp,trestbps,chol,
        fbs,restecg,thalach,
        exang,oldpeak,slope,
        ca,thal
        ]])
    data = scaler.transform(data)
    prediction = model.predict(data)
    if prediction[0]==1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease")