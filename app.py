import streamlit as st
import pandas as pd
import pickle as pk
import numpy as np

pickle_in = open('model_pickle','rb')
svc = pk.load(pickle_in)
def prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    prediction = svc.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    print(prediction)
    return prediction
def main():
    st.title("Diabetes Symptoms ")


    html_temp = """
    <div style="background-color:orange; padding:10px">
    <h2 style="color:red;text-align:center;">Streamlit Diabetes Predictor </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Pregnancies = st.text_input("Pregnancies", "ENTER_DIGIT")
    Glucose = st.text_input("Glucose", "ENTER_DIGIT")
    BloodPressure = st.text_input("BloodPressure", "ENTER_DIGIT")
    SkinThickness = st.text_input("SkinThickness", "ENTER_DIGIT")
    Insulin = st.text_input("Insulin", "ENTER_DIGIT")
    BMI = st.text_input("BMI", "ENTER_DIGIT")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction", "ENTER_DIGIT")
    Age = st.text_input("Age", "ENTER_DIGIT")


    result = ""
    if st.button("Predict"):
        result = prediction(int(Pregnancies),int(Glucose),int(BloodPressure),int(SkinThickness),int(Insulin),float(BMI),float(DiabetesPedigreeFunction),int(Age))
        print('result',result[0])
        if result[0] == 1:
            result2 = 'patient has diabities'
            st.success('The output is {}'.format(result2))
        elif result[0] == 0:
            result2 = 'patient does\'nt have diabities'
            st.success('The output is {}'.format(result2))
        else:
            result2 = 'please try again'
            st.success('The output is {}'.format(result2))





main()
