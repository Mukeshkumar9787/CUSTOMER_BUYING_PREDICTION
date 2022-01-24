# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:00:01 2022

@author: Admin
"""

import streamlit as st
import pickle

pickle_in=open("dtc_classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def customer_predict(age,salary):
    prediction=classifier.predict([[age,salary]])
    return "THE IS THE PREDICTION VALUE IS " + str(prediction)

def main():
    st.title("CUSTOMER BUYING BEHAVIOUR")
    html_temp = """
    <div style="backgroud-color:red;padding:15px">
    <h2 style="color:black;text-align;center;">Streamlit customer buying behaviour </h2>
    </div>
    """    
    st.markdown(html_temp,unsafe_allow_html=True)
    age=st.text_input("age")
    salary=st.text_input("salary")
    result=""
    if st.button("Predict"):
        result=customer_predict(age, salary)
    st.success(result)
    if st.button("ABOUT"):
        st.text("the model is:")
        st.text(type(classifier))
    
if __name__=='__main__':
    main()