import streamlit as st
import pandas as pd
import requests
import json


data = pd.read_csv('your_dataset.csv')  


passenger_ids = data['PassengerId'].unique()
pclasses = data['Pclass'].unique()
survived_options = [0, 1] 


input_passenger_id = st.selectbox("Passenger ID", passenger_ids)
input_pclass = st.selectbox("Pclass", pclasses)
input_survived = st.selectbox("Survived", survived_options)

if st.button("Predict"):
    rest_url = "http://51.142.165.55:80/api/v1/service/myendpoint/score"
    key = "eGIVsccxv3mNsB673b8gvn4Bkh&Xrww"

    data = {
        "Inputs": {
            "input1": {
                "PassengerId": input_passenger_id,
                "Pclass": input_pclass,
                "Survived": input_survived
            }
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + key
    }

    response = requests.post(rest_url, data=json.dumps(data), headers=headers)

    st.write(response.content)
