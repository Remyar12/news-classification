import streamlit as st
import joblib

# Load the trained model
model=joblib.load("news-classification-model.pkl")

# Define news labels
news_labels={'0': 'Technical', '1': 'Business','2':'Sports','3':'Entertainment','4':'Politics'}

# Create Streamlit app
st.title("News Classification")

# Input text area
user_input= st.text_area("Enter the you text here:")

# Prediction button
if st.button("Predict"):
    # Perform news prediction
    print(user_input)
    predicted_label=model.predict([user_input])[0]
    print("Predicted Label:" + str(predicted_label))
    predicted_news_label=news_labels[str(predicted_label)]

    # Display predicted sentiment
    st.info(f"Predicted Sentiment: {predicted_news_label}")
