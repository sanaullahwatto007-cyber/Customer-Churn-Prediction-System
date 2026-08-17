# Customer Churn Prediction System

## Project Overview

This project is a Machine Learning based Customer Churn Prediction System.

It predicts whether a customer is likely to churn or not using different supervised learning algorithms.

## Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest
- Naive Bayes
- KNN
- SVM
- Gradient Boosting
- XGBoost
- AdaBoost
- Bagging
- Extra Trees

## Best Model

**Gradient Boosting**

**Accuracy:** 86.4%

**ROC-AUC:** 0.872

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Project Workflow

**EDA → Preprocessing → Train-Test Split → Pipeline → Model Training → Model Evaluation → Best Model Selection → Streamlit App**

## Features

The system takes the following customer information:

- Credit Score
- Country
- Gender
- Age
- Tenure
- Balance
- Products Number
- Credit Card
- Active Member
- Estimated Salary

## Files

- `churn.py` — Streamlit application
- `customer_churn_model.pkl` — Trained Gradient Boosting model
- `customer_churn_features.pkl` — Model features
- `requirements.txt` — Required Python libraries
- `Customer Churn Prediction System.ipynb` — Complete ML project notebook

## How to Run

```bash
pip install -r requirements.txt

STREMLIT APP
LIVE DEMO
