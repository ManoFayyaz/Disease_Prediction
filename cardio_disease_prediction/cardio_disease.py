import streamlit as st
import requests

st.title('Cardiovascular Disease Prediction Web-app')
st.subheader('Enter the required details to predict the risk of cardiovascular disease')
st.write("This application predicts the risk of cardiovascular disease based on user-provided health metrics.")

st.subheader('Input Medical Features')

thal = st.number_input("thal", min_value=0.0)
ca = st.number_input("ca", min_value=0.0)
cp = st.number_input("cp", min_value=0.0)
thalach = st.number_input("thalach", min_value=0.0)
oldpeak = st.number_input("oldpeak", min_value=0.0)
exang = st.number_input("exang", min_value=0)
age = st.number_input("age", min_value=1)
chol = st.number_input("chol", min_value=0)
trestbps = st.number_input("trestbps", min_value=0)
slope = st.number_input("slope", min_value=0)
sex = st.radio("sex (0 = female, 1 = male)", [0, 1])
restecg = st.number_input("restecg", min_value=0)
fbs = st.number_input("fbs", min_value=0)

if st.button("Predict"):
    with st.spinner("Predicting......"):

        data = {
            "thal": thal,
            "ca": ca,
            "cp": cp,
            "thalach": thalach,
            "oldpeak": oldpeak,
            "exang": exang,
            "age": age,
            "chol": chol,
            "trestbps": trestbps,
            "slope": slope,
            "sex": sex,
            "restecg": restecg,
            "fbs": fbs }
        
        url="http://127.0.0.1:5000/cardiopredict"

        response=requests.post(url,json=data)


        if response.status_code == 200:
            result = response.json()
            
            if result['prediction'] == 1:
                st.error("High risk of cardiovascular disease detected.")
            else:
                st.success("Low risk of cardiovascular disease detected.")
            # st.success(f"Prediction: {result['prediction']}")
            st.write(f"Probability: {result['probability']*100:.2f}%")
        else:
            st.error("Error communicating with backend.")