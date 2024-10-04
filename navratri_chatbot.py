import streamlit as st
import nltk # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.svm import SVC # type: ignore
import numpy as np
from PIL import Image

# Load the NLTK data
nltk.download('punkt')

# Displaying the Happy Navratri greeting
st.title("Happy Navratri!")
st.write("Wishing you a joyful and prosperous Navratri!🙏✨")

# Load and display the image
image = Image.open("C:\\Users\\ARYAN\\Desktop\\Framework\\Durga Puja.jpg")

st.image(image, caption='Happy Navratri!')

# Chatbot interaction
user_input = st.text_input("How are you celebrating this Navratri?")
if user_input:
    st.write(f"That's wonderful! Enjoy the festival, and may Goddess Durga bless you with strength and happiness.")


# Training data: simple Navratri related FAQs and responses
train_data = {
    "What is Navratri?": "Navratri is a Hindu festival celebrated for nine days, honoring Goddess Durga.",
    "How many days is Navratri celebrated?": "Navratri is celebrated for nine days.",
    "Why is Navratri celebrated?": "Navratri celebrates the victory of good over evil, particularly the victory of Goddess Durga over the demon Mahishasura.",
    "What are the colors of Navratri?": "Each day of Navratri is associated with a different color, such as yellow, green, grey, and more.",
    "When does Navratri start?": "Navratri typically starts in late September or early October."
}

# Preprocess training data
questions = list(train_data.keys())
answers = list(train_data.values())

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(questions)

# Train the classifier (SVM)
model = SVC(kernel='linear')
model.fit(X_train, range(len(questions)))

# Function to predict the answer
def get_response(user_input):
    user_input_vect = vectorizer.transform([user_input])
    prediction = model.predict(user_input_vect)
    return answers[prediction[0]]

# Streamlit UI
st.title("Happy Navratri Chatbot!")
st.write("Ask me anything about Navratri!")

# User input
user_input = st.text_input("You:")

# Display response
if user_input:
    response = get_response(user_input)
    st.write(f"Chatbot: {response}")




