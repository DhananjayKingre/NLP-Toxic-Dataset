# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vbW_PQ6vgew-1y1Oarydjg5KclEq1c1i
"""

import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import joblib
from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

model = joblib.load(open("./multi_label_classifier.pkl", "rb"))

# Load the vectorizer from the file
vectorizer = load('vectorizer..pkl')

# Create a Streamlit web app
st.title("Multi-Label Comment Classification")


st.title("Multi-Label Comment Classification")


user_input = st.text_area("Enter your comment here:")

if st.button("Predict"):
    if user_input:
        # Preprocess the user's input text using the loaded CountVectorizer
        user_input_cv = vectorizer.transform([user_input])

        
        predictions = model.predict(user_input_cv)

 
        label_names = {
            0: 'Toxic',
            1: 'Severe Toxic',
            2: 'Obscene',
            3: 'Threat',
            4: 'Insult',
            5: 'Identity Hate',
            6:  'clean'
        }


        st.subheader("Predicted Labels:")
        for i, label_id in enumerate(label_names):
            label_name = label_names[label_id]
            prediction = "Yes" if predictions[0, i] == 1 else "No"
            st.write(f"{label_name}: {prediction}")


if __name__ == '__main__':
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.set_option('deprecation.showPyplotGlobalUse', False)