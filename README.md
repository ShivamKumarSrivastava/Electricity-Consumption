# ⚡ Power Consumption Prediction App

A Machine Learning web application built using **Streamlit** that predicts electricity power consumption for different zones based on weather and time-related features.

🔗 🔗 **Live App:** [Click Here to Try the App](https://electricity-consumption-7deafu6weilkfweqjzq6bf.streamlit.app/)


---

## 📌 Project Overview

This application predicts power consumption (in KW) for three different zones using trained Machine Learning models.

The prediction is based on:

- Temperature
- Humidity
- Wind Speed
- Diffuse Solar Radiation
- Direct Solar Radiation
- Hour of the Day
- Day of the Week
- Month
- Season

---

## 🚀 Features

- Interactive Streamlit web interface
- Zone-wise prediction (Zone1, Zone2, Zone3)
- Clean and user-friendly dashboard
- Real-time prediction
- Machine Learning model integration

---

## 🧠 Machine Learning Model

- Algorithm Used: Random Forest Regressor
- Trained separately for each zone
- Saved using `joblib`
- Input features encoded and structured before prediction

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas
- Joblib

---

## 📂 Project Structure

```
Power-Consumption-Prediction/
│
├── data/
│   └── powerconsumption.csv
│
├── models/
│   ├── zone1_model.pkl
│   ├── zone2_model.pkl
│   └── zone3_model.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Training.ipynb
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```


---

## ▶ How to Run Locally

```bash
git clone https://github.com/ShivamKumarSrivastava/Electricity-Consumption.git
cd Electricity-Consumption
pip install -r requirements.txt
streamlit run streamlit_app.py

```

## 🌍 Deployment

This application is deployed using **Streamlit Community Cloud**.

---

## 📊 Future Enhancements

- Add evaluation metrics (R², MAE, RMSE)
- Add feature importance visualization
- Add historical data visualization dashboard
- Implement model comparison
- Dockerize the application for production deployment

---

## 👨‍💻 Author

**Shivam Kumar**  
Machine Learning Student 🚀  

---

⭐ If you found this project useful, consider giving it a star!