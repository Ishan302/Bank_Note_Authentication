


import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image



pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(variance,skewness,curtosis,entropy):
    

   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("Skewness","Type Here")
    curtosis = st.text_input("Kurtosis","Type Here")
    entropy = st.text_input("Entropy","Type Here")
    result=""

    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        if result == 0:
            st.error('The Banknotes are Forged ⚔️')
        else:

            st.success('The Banknotes are Genuine ✔️')
           
    if st.button("About"):

        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
