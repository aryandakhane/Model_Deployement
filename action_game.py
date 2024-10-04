import streamlit as st
import random
import time
from streamlit_lottie import st_lottie
import requests

# Lottie function to load animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a lottie animation (replace with an action-oriented animation link)
lottie_action = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_cw5x0oxj.json")

# Title of the game
st.title("⚔️ Streamlit Action Game 🎮")

# Display the animation
st_lottie(lottie_action, speed=1, height=300, key="action_animation")

# Game instructions
st.write("Dodge the obstacles and collect points! Move using the buttons below.")

# Game State Variables
points = 0
obstacle_position = random.randint(1, 3)

# Buttons for user input
col1, col2, col3 = st.columns(3)
left = col1.button("Left ⬅️")
middle = col2.button("Stay ⏺️")
right = col3.button("Right ➡️")

# Action based on input
if left:
    user_position = 1
elif middle:
    user_position = 2
elif right:
    user_position = 3
else:
    user_position = 2  # default start position

# Check if the player dodged the obstacle
if user_position == obstacle_position:
    st.error("You hit an obstacle! Game Over.")
else:
    points += 1
    st.success(f"Nice move! You dodged the obstacle. Your points: {points}")
    
# Update obstacle position for the next round
obstacle_position = random.randint(1, 3)

# Button to restart the game
if st.button("Restart Game"):
    points = 0
    st.experimental_rerun()
