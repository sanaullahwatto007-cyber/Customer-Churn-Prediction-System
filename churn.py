
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("customer_churn_model.pkl")

# Page Title
st.title("Customer Churn Prediction System")
st.write("Enter customer information to predict churn.")

# Customer Inputs
credit_score = st.number_input(
    "Credit Score", 300, 900, 650
)

country = st.selectbox(
    "Country",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

age = st.number_input(
    "Age", 18, 100, 40
)

tenure = st.number_input(
    "Tenure", 0, 10, 5
)

balance = st.number_input(
    "Balance", min_value=0.0, value=100000.0
)

products_number = st.number_input(
    "Products Number", 1, 4, 1
)

credit_card = st.selectbox(
    "Credit Card",
    [0, 1]
)

active_member = st.selectbox(
    "Active Member",
    [0, 1]
)

estimated_salary = st.number_input(
    "Estimated Salary", min_value=0.0, value=50000.0
)

# Prediction
if st.button("Predict Churn"):

    new_customer = pd.DataFrame([{
        "credit_score": credit_score,
        "country": country,
        "gender": gender,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": credit_card,
        "active_member": active_member,
        "estimated_salary": estimated_salary
    }])

    prediction = model.predict(new_customer)[0]

    probability = model.predict_proba(new_customer)[0][1]

    if prediction == 1:
        st.error("Customer will churn")
    else:
        st.success("Customer will not churn")

    st.write(
        f"Churn Probability: {probability * 100:.2f}%"
    )
