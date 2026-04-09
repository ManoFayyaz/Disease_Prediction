from flask import Flask,request,redirect,url_for,jsonify
import joblib
import numpy as np


app=Flask(__name__)


model=joblib.load('rf_model.pkl')

feature_names=["thal", "ca", "cp", "thalach", "oldpeak", "exang", "age",
    "chol", "trestbps", "slope", "sex", "restecg", "fbs"]


@app.route('/cardiopredict', methods=['POST'])
def cardio_predict():
    data=request.json

    x=[data[features] for features in feature_names]
    x=np.array(x).reshape(1,-1) 

    prediction=model.predict(x)[0]
    probability = model.predict_proba(x)[0][1]

    return jsonify({
        "prediction": int(prediction),
        "probability": float(probability)
    })

if __name__=="__main__":
    app.run(debug=True)
