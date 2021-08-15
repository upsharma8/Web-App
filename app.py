from flask import Flask,render_template
from flask import request
import os
from keras.models import load_model
from keras.preprocessing import image
import numpy as  np
from PIL import Image

app=Flask("predict")

UPLOAD_FOLDER='Images'

def predictfunc(image_file):
    path=UPLOAD_FOLDER
    test_image=image.load_img(path+'/'+image_file.filename,target_size=(64,64))
    test_img_arr=image.img_to_array(test_image)
    test_img_arr_4d=np.expand_dims(test_img_arr,axis=0)
    model=load_model("covid-19.h5")
    p= model.predict(test_img_arr_4d)
    return round(p[0][0])

    
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html") 

@app.route('/covid19',methods=['GET','POST'])
def upload_predict():
    prediction=""
    
    if request.method=="POST":
  
        image_file=request.files["image"]
        if image_file:
            image_location=os.path.join(UPLOAD_FOLDER, image_file.filename)
            image_file.save(image_location)
            print(image_file.filename)
            a=predictfunc(image_file)
            if a==0:
                prediction="Covid-19 is Predicted For You"
                
            elif a==1:
                prediction="covid-19 is not Preicted for you"
                
    return render_template('covid19.html',prediction=prediction)	

@app.route('/about')
def aboutus():
    return render_template("about.html")

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")



@app.route("/output",methods=["GET"])
def predict():
    
    a1=(float)(request.values.get("x1"))
    a2=float(request.values.get("x2"))
    a3=float(request.values.get("x3"))
    a4=float(request.values.get("x4"))
    a5=float(request.values.get("x5"))
    a6=float(request.values.get("x6"))
    a7=float(request.values.get("x7"))

    a8=float(request.values.get("x8"))
    m=load_model("diabetes_model.h5")

    output=m.predict([[a1,a2,a3,a4,a5,a6,a7,a8]])
    if output < 0.5:
        return("Diabetes is not predicted for you")
    else:
        return("Diabetes is predicted for you")



app.run(host="0.0.0.0",debug=True,port=5000)
