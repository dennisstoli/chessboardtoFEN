import streamlit as st
from keras.models import load_model 
@st.cache
def load_my_model():
    model = load_model('model.h5')
    model.summary()

    return model
