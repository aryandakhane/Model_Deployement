import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animations
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        return None

# Lottie URL for weather animation
lottie_url = "https://assets7.lottiefiles.com/packages/lf20_jcikwtux.json"  # Replace with working URL


# Set page title
st.title("Animated Weather Dashboard 🌤️")

# Add a header
st.header("Today's Weather Forecast")

# Show animation if available
if lottie_url:
    st_lottie(lottie_url, height=300, width=300)
else:
    st.error("Error loading animation!")

# Display placeholder weather data
st.subheader("City: Nagpur")
st.write("Temperature: 18°C")
st.write("Condition: Cloudy with a chance of rain 🌧️")
st.write("Humidity: 70%")
st.write("Wind Speed: 12 km/h")
