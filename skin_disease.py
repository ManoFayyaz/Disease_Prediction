import streamlit as st
import requests

st.title('Skin Disease Detection Web-app')
st.subheader('Upload the image of skin disease to predict')
st.write("Please upload a clear image of the affected skin area for accurate prediction.")

st.write('Major Skin Diseases Covered: Basal Cell Carcinoma, Melanoma, Actinic Keratoses, Benign Keratosis-like Lesions, Dermatofibroma, Melanocytic Nevi, Vascular Lesions')


pic=st.file_uploader("Upload a picture of skin disease", type=["jpg","png","jpeg"])

if pic is not None:
    st.image(pic,caption="Picture Uploaded Successfully!")

    if st.button("Predict"):
        with st.spinner("Predicting......"):

            files = {"file": pic.getvalue()}

            url="https://diseaseprediction-production-f07e.up.railway.app/predict"
            response=requests.post(url,files=files)    

            if response.status_code==200:
                result=response.json()["prediction"]
                st.success(f"Disease detected to be  {result} ")
            else:
                st.error("Bcakend Issue!")
