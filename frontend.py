import streamlit as st
import requests

API_URL="http://127.0.0.1:8000/predict"
st.title("loan_status_prediction")
st.markdown("Enter your detail below")


# Input fields

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

married = st.selectbox(
    "Married",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0.0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0
)

loan_amount_term = st.number_input(
    "Loan Amount Term",
    min_value=0
)

credit_history = st.selectbox(
    "Credit History",
    [0, 1]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Rural", "Semiurban"]
)

if st.button("predict loan status"):
  

    input_data = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_amount_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }
    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code==200:
         result=response.json()
         st.success(f"loan_status:{result['loan_status']}")
        else:
           st.error(f"api error:{response.status_code}-{response.text}")
    except requests.exceptions.ConnectionError:
       st.error("error")

