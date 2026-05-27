# 🏦 Loan Status Prediction System

## 📌 About the Project

This project predicts whether a loan application will be **Approved** or **Rejected** using Machine Learning techniques.

The system is built with:

- 🧠 Machine Learning Model
- ⚡ FastAPI Backend API
- 🎨 Streamlit Frontend Web App

Users can enter applicant details through the Streamlit interface, and the FastAPI backend processes the data and returns the prediction result.

---

# 🚀 Features

✅ Loan approval prediction  
✅ FastAPI REST API integration  
✅ Interactive Streamlit frontend  
✅ Data preprocessing pipeline  
✅ Scalable ML deployment structure  
✅ Input validation using Pydantic  

---

# 🧠 Machine Learning Workflow

1. Data Loading  
2. Data Cleaning  
3. Handling Missing Values  
4. Feature Encoding using OneHotEncoder  
5. Feature Scaling using StandardScaler  
6. Model Training  
7. Model Evaluation  
8. API Deployment using FastAPI  
9. Frontend Integration using Streamlit  

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- FastAPI
- Streamlit
- Pydantic
- Pickle

---

# 📂 Project Structure

```bash
loan-status-prediction/
│
├── app.py                     # FastAPI backend
├── frontend.py                # Streamlit frontend
├── Loan_Status_Prediction.ipynb
├── train.csv
├── loan_model1.pkl
├── scaler.pkl
├── model_columns.pkl
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Indrapalsingh8241/loan_status_prediction
cd loan-status-prediction
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

# ▶️ Run the Project

## Start FastAPI Backend

```bash
uvicorn app:app --reload
```

Backend runs at:

```bash
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

```bash
streamlit run frontend.py
```

Frontend runs at:

```bash
http://localhost:8501
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

## Health Check Endpoint

```http
GET /Health
```

---

## Prediction Endpoint

```http
POST /predict
```

---

# 📊 Model Evaluation

Evaluation metrics used:

- Accuracy Score
- Confusion Matrix

---

# 💡 Future Improvements

- Hyperparameter tuning
- Model deployment on cloud
- Docker support
- Authentication system
- Database integration
- Better UI/UX

---

# 👨‍💻 Author

## Indrapal Singh

Machine Learning & Backend Developer

---