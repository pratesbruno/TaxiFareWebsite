import streamlit as st
import datetime
import requests


'''
# TaxiFareModel front
'''

st.markdown('''
Please choose the parameters.
''')

pickup_datetime = st.date_input(
    "Choose pickup date",
    datetime.date(2019, 7, 6))

pickup_datetime = str(pickup_datetime) + ' 17:18:00 UTC'

pickup_longitude = st.number_input('Choose pickup longitude')
pickup_latitude = st.number_input('Choose pickup latitude')
dropoff_longitude = st.number_input('Choose dropoff longitude')
dropoff_latitude = st.number_input('Choose dropoff latitude')
passenger_count = st.number_input('Choose passenger count')

params = {
            "key": '2013-07-06 17:18:00.000000119',
            "pickup_datetime": str(pickup_datetime),   #'2013-07-06 17:18:00 UTC',
            "pickup_longitude": float(pickup_longitude),
            "pickup_latitude": float(pickup_latitude),
            "dropoff_longitude": float(dropoff_longitude),
            "dropoff_latitude": float(dropoff_latitude),
            "passenger_count": float(passenger_count)
             }
'''
## Click button for prediction
'''

url = f'https://image-name-sgdo4nfp4a-ew.a.run.app/predict_fare/'

if st.button('Predict Fare'):
    response = requests.get(url, params=params)
    st.write(params)
    st.write('Prediction:', response.json()['prediction'])
else:
    st.write('I was not clicked 😞')
