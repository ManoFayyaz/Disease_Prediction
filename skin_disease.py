import streamlit as st
import requests

st.title('Skin Disease Detection Web-app')

pic=st.file_uploader("Upload a picture of skin disease", type=["jpg","png","jpeg"])

if pic is not None:
    st.image(pic,caption="Picture Uploaded Successfully!")

    if st.button("Predict"):
        with st.spinner("Predicting......"):

           files = {"file": pic.getvalue()}

            url="http://127.0.0.1:5000/predict"
            response=requests.post(url,files=files)    

            if response.status_code==200:
                result=response.json()["prediction"]
                st.success(f"Disease detected to be  {result} ")
            else:
                st.error("Bcakend Issue!")
