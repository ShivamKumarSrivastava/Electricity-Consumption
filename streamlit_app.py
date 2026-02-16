import streamlit as st
import joblib
import numpy as np
from typing import Dict

st.set_page_config(page_title="Power Prediction", layout="centered")

@st.cache_resource
def load_models() -> Dict[str, object]:
    return {
        "Zone1": joblib.load("models/zone1_model.pkl"),
        "Zone2": joblib.load("models/zone2_model.pkl"),
        "Zone3": joblib.load("models/zone3_model.pkl"),
    }

models = load_models()

day_map = {
    'Monday':0,
    'Tuesday':1,
    'Wednesday':2,
    'Thursday':3,
    'Friday':4,
    'Saturday':5,
    'Sunday':6
}

season_map = {
    'Winter':0,
    'Autumn':1,
    'Summer':2,
    'Monsoon':3
}

st.title("POWER CONSUMPTION PREDICTION")

zone = st.sidebar.selectbox("Select Zone", ["Select Zone","Zone1", "Zone2", "Zone3"])

st.markdown("### 🌤 Weather Conditions")

Temperature = st.number_input("Temperature in Celsius", value=25.0)
Humidity = st.number_input("Humidity in Percentage", value=50.0)
WindSpeed = st.number_input("Wind Speed in (meter/second)", value=5.0)
GeneralDiffuseFlows = st.number_input("General Diffuse Flows (Scatter Solar Radiation) in (W/m2)", value=100.0)
DiffuseFlows = st.number_input("Diffuse Flows (Direct Solar Radiation) in (W/m2)", value=50.0)

st.markdown("### 🕒 Time Information")

Hour = st.slider("Hour", min_value=0, max_value=23, value=12)
Month = st.slider("Month", min_value=1, max_value=12, value=6)

Day_name = st.selectbox("Day", list(day_map.keys()))
Season_name = st.selectbox("Season", list(season_map.keys()))

Day = day_map[Day_name]
Season = season_map[Season_name]

input_data = np.array([[ 
    Temperature,
    Humidity,
    WindSpeed,
    GeneralDiffuseFlows,
    DiffuseFlows,
    Hour,
    Day,
    Month,
    Season
]])

if st.button("Predict Power Consumption"):

    if zone == "Select Zone":
        st.warning("Please select a zone first.")
    else:
        prediction = models[zone].predict(input_data)
        st.success(f"Predicted Power Consumption for {zone}: {prediction[0]:.2f} KW")

