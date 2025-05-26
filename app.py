import streamlit as st
import requests
from pprint import pprint

API_KEY = '42743ea5cb7b455ea9e63937242909'

st.set_page_config(page_title="Weather App", page_icon="☁️", layout="wide")
st.title("☁️ Weather App")

city = st.text_input("Enter the city name:", placeholder="e.g. New York", key="city_input")

if st.button("Get Weather"):
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        pprint(weather_data)  # Optional: for debugging in console
        
        temp_c = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        wind_kph = weather_data['current']['wind_kph']

        # Display styled weather info with dynamic data
        st.markdown(f"""
            <div style="
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                margin: 40px auto;
                width: 400px;
                padding: 30px;
                border-radius: 15px;
                background: rgba(255, 255, 255, 0.15);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.18);
                font-family: 'Segoe UI', sans-serif;
                color: white;
                text-align: center;
            ">
                <h2 style="margin-bottom: 20px;">🌦️ Current Weather in {city.title()}</h2>
                <p style="font-size: 20px;">🌡️ Temperature: <strong>{temp_c} °C</strong></p>
                <p style="font-size: 20px;">💧 Humidity: <strong>{humidity} %</strong></p>
                <p style="font-size: 20px;">🌬️ Wind: <strong>{wind_kph} km/h</strong></p>
            </div>
        """, unsafe_allow_html=True)

