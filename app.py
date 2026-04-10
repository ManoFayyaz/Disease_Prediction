from flask import Flask,render_template,request,redirect,url_for,jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io
import os

app=Flask(__name__)

model=load_model('skin_disease_model.h5')

def preprocess(image):
    image=image.resize((28,28))
    image=np.array(image)/255.0
    image=np.expand_dims(image,axis=0)
    return image

def explain_prediction(predicted_class):
    match predicted_class:
        case 0:
            return (
                    "Actinic Keratoses: Precancerous lesions caused by chronic sun exposure. "
                    "Usually rough, scaly patches and can develop into squamous cell carcinoma if untreated. "
                    "Treatment: Dermatologists commonly use cryotherapy (freezing), topical creams, or light-based therapies. "
                    "Sun protection is essential to prevent worsening."
            )       
        case 1:
            return (
                    "Basal Cell Carcinoma: A common type of skin cancer arising from basal cells. "
                    "Often appears as pearly or waxy bumps with visible vessels. "
                    'Treatment: Usually removed through minor surgery. Dermatologists may use excision, Mohs surgery, '
                    'or topical treatments depending on severity.'
                    )      
        case 2:
            return (
                "Benign Keratosis-like Lesions: Non-cancerous growths that appear as scaly or wart-like patches. "
                "Harmless but may be cosmetically concerning. "
                "Treatment: Generally no treatment needed. Removal options include cryotherapy or minor procedures if desired."
            )
        case 3:
             return (
                "Dermatofibroma: A benign skin nodule usually found on limbs; firm and sometimes itchy. "
                "Treatment: Typically harmless and requires no treatment. Removal possible via minor surgery if symptomatic."
            )
        case 4:
            return (
                "Melanocytic Nevi (Moles): Benign clusters of melanocytes that vary in size and color. "
                "Usually harmless. "
                "Treatment: No treatment required unless the mole changes shape/color or becomes symptomatic — then evaluation and possible removal is recommended."
            )
        case 5:
            return (
                "Melanoma: A serious and potentially aggressive skin cancer arising from melanocytes. "
                "Often appears as an irregular, changing mole. "
                "Treatment: Requires urgent attention. Standard treatment includes surgical removal and, in advanced cases, "
                "targeted or immunotherapy (as determined by specialists). Early detection is critical."
            )
        case 6:
              return (
                "Vascular Lesions: Benign growths or clusters of blood vessels appearing red or purple. "
                "Usually harmless and may fade naturally. "
                "Treatment: Often no treatment required. Options like laser therapy may be used for cosmetic improvement."
            )
        case _:
            return "Unknown class"



@app.route("/predict",methods=["POST"])
def predict():
   if 'file' not in request.files:
       return({"error":"No image uploaded"}),400
   
   file=request.files['file']
   img=Image.open(io.BytesIO(file.read()))
   processed=preprocess(img)
   prediction=model.predict(processed)
   result=np.argmax(prediction)

   result=explain_prediction(result)
   return jsonify({"prediction": result})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)






# #URL Routing
# @app.route("/",methods=["GET"])
# def welcome():
#     return "<h1>Welcome to my app</h1>"

# @app.route("/index",methods=["GET"])
# def index():
#     return "Index page"

# #variable rule
# @app.route('/success/<int:score>')
# def success(score):
#     # return "Passed!!!   Score: "+ str(score)
#     return render_template('success.html',score=score)


# @app.route('/fail/<int:score>')
# def fail(score):
#     return "Fail!!! Score: "+ str(score)


# @app.route('/form',methods=["GET","POST"])
# def form():
#     if request.method=="GET":
#         return render_template('form.html')
#     else:
#         maths=float(request.form["maths"])
#         history=float(request.form["history"])
#         english=float(request.form["english"])

#         total_marks=maths+history+english
#         avg_marks=round((maths+history+english)/3,3)
        
#         res=""

#         if avg_marks>=50:
#             res="success"
#         else:
#             res="fail"    

#         return(redirect(url_for(res,score=avg_marks)))
#         # return render_template('form.html',avg=avg_marks,total=total_marks)

# @app.route('/api', methods=['POST'])
# def calculate_sum():
#     data = request.get_json()

#     a_val = float(data['a'])
#     b_val = float(data['b'])

#     return jsonify({"sum": a_val + b_val})


