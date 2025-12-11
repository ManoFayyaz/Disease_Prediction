from flask import Flask,render_template,request,redirect,url_for,jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

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
            return "Actinic Keratoses: Precancerous lesions caused by chronic sun exposure.Usually rough, scaly, or crusty patches. Can develop into squamous cell carcinoma if untreated."
        case 1:
            return "Basal Cell Carcinoma: A common type of skin cancer that arises from basal cells in the epidermis. Often appears as pearly or waxy bumps, sometimes with visible blood vessels."
        case 2:
            return "Benign Keratosis-like Lesions: Non-cancerous skin growths that may appear as scaly, wart-like patches. They are usually benign but can be cosmetically concerning."
        case 3:
            return "Dermatofibroma: A benign skin tumor that appears as a firm, raised nodule. Often found on the limbs and can be itchy or tender."
        case 4:
            return "Melanocytic Nevi: Commonly known as moles, these are benign proliferations of melanocytes. They can vary in color and size and are usually harmless."
        case 5:
            return "Melanoma: A serious form of skin cancer that originates in melanocytes. It can appear as an irregular mole or dark spot and has a high potential to spread if not detected early."
        case 6:
            return "Vascular Lesions: Benign growths of blood vessels that can appear as red or purple marks on the skin. They are usually harmless and may fade over time."
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


if __name__=="__main__":
    app.run(debug=True)






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


