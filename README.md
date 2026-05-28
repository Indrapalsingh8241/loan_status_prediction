# 🏦 Loan Status Prediction System

A complete end-to-end Machine Learning deployment project that predicts whether a loan application will be **Approved** or **Rejected** using applicant information.

The project integrates:

* 🧠 Machine Learning Model
* ⚡ FastAPI Backend
* 🎨 Streamlit Frontend
* 🐳 Docker Containerization

---

# 🚀 Live Features

✅ Loan Approval Prediction
✅ FastAPI REST API
✅ Interactive Streamlit UI
✅ Pydantic Input Validation
✅ Dockerized Deployment
✅ ML Preprocessing Pipeline
✅ Scalable Backend Architecture

---

# 🧠 Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Missing Value Handling
4. Exploratory Data Analysis (EDA)
5. Feature Encoding
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Model Serialization using Pickle
10. API Deployment using FastAPI
11. Frontend Integration using Streamlit

---

# 🛠️ Tech Stack

## Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn

## Backend

* FastAPI
* Pydantic
* Uvicorn

## Frontend

* Streamlit

## Deployment

* Docker

---

# 📂 Project Structure

```bash
loan_status_prediction/
│
├── app.py                       # FastAPI backend
├── frontend.py                  # Streamlit frontend
├── start.sh                     # Runs FastAPI + Streamlit
├── Dockerfile                   # Docker configuration
├── Loan_Status_Prediction.ipynb
├── train.csv
├── loan_model1.pkl
├── scaler.pkl
├── model_columns.pkl
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Indrapalsingh8241/loan_status_prediction.git

cd loan_status_prediction
```

---

## 2️⃣ Create Virtual Environment

```bash
python3 -m venv myvenv

source myvenv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

## Start FastAPI Backend

```bash
uvicorn app:app --reload
```

FastAPI runs on:

```bash
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

```bash
streamlit run frontend.py
```

Streamlit runs on:

```bash
http://localhost:8501
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t loan_prediction .
```

---

## Run Docker Container

```bash
docker run -p 8501:8501 -p 8000:8000 loan_prediction
```

---

# 🔌 API Endpoints

## Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "loan status prediction"
}
```

---

## Health Check

```http
GET /Health
```

---

## Prediction Endpoint

```http
POST /predict
```

---

# 📥 Sample Prediction Request

```json
{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "0",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 2000,
  "LoanAmount": 150,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": "Urban"
}
```

---

# 📤 Sample Response

```json
{
  "loan_status": "Approved"
}
```

---

# 📊 Model Evaluation

Evaluation metrics used:

* Accuracy Score
* Confusion Matrix
* Classification Report

---

# 💡 Future Improvements

* Cloud Deployment
* CI/CD Pipeline
* Authentication & Authorization
* Database Integration
* Model Monitoring
* Better UI/UX
* Kubernetes Deployment

---

# 👨‍💻 Author

## Indrapal Singh

Machine Learning | FastAPI | Streamlit | Docker

GitHub:
https://github.com/Indrapalsingh8241
