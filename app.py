import streamlit as st
import joblib 
import pandas as pd


model=joblib.load("car.pkl")
st.title("Car Price Prediction")
mileage=st.number_input("Enter mileage:")
age=st.number_input("Enter age:")
df=pd.DataFrame([[mileage,age]],columns=["Mileage","Age(yrs)"])
if st.button("Predict"):
    st.success(round(model.predict(df)[0],2))
    #st.write(df)