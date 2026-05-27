from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Literal,Annotated,Dict
import pandas as pd
import pickle

with open("loan_model1.pkl",'rb') as f:
    model=pickle.load(f)

with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

app=FastAPI()

# pydantic model to validate incoming data

class UserInput(BaseModel):

    Gender: Annotated[
        Literal['Male', 'Female'],
        Field(description='Gender of applicant')
    ]

    Married: Annotated[
        Literal['Yes', 'No'],
        Field(description='Marital status')
    ]

    Dependents: Annotated[
        Literal['0', '1', '2', '3+'],
        Field(description='Number of dependents')
    ]

    Education: Annotated[
        Literal['Graduate', 'Not Graduate'],
        Field(description='Education status')
    ]

    Self_Employed: Annotated[
        Literal['Yes', 'No'],
        Field(description='Self employed status')
    ]

    ApplicantIncome: Annotated[
        int,
        Field(gt=0, description='Applicant income')
    ]

    CoapplicantIncome: Annotated[
        float,
        Field(ge=0, description='Coapplicant income')
    ]

    LoanAmount: Annotated[
        float,
        Field(gt=0, description='Loan amount')
    ]

    Loan_Amount_Term: Annotated[
        int,
        Field(gt=0, description='Loan amount term')
    ]

    Credit_History: Annotated[
        Literal[0, 1],
        Field(description='Credit history')
    ]

    Property_Area: Annotated[
        Literal['Urban', 'Rural', 'Semiurban'],
        Field(description='Property area')
    ]

@app.post("/predict")
def loan_status(data: UserInput):

    
    data_dict = data.model_dump()

    # dict -> dataframe
    df = pd.DataFrame([data_dict])

    # apply same encoding
    df = pd.get_dummies(df)

    # match training columns
    df = df.reindex(columns=model_columns, fill_value=0)

    # apply scaling
    df = scaler.transform(df)

    # prediction
    prediction = model.predict(df)[0]

    loan_status = "Approved" if prediction else "Rejected"

    return JSONResponse(status_code=200,content={
        "loan_status": loan_status}
    )