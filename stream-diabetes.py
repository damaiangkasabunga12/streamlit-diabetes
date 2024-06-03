import pickle
import streamlit as st

#membaca model
diabetes_model=pickle.load(open('C:/Users/damai/OneDrive/Desktop/Big project ssd/diabetes_model.sav','rb'))

#judul web
st.title('Prediksi Pasien Terkena Diabetes')

