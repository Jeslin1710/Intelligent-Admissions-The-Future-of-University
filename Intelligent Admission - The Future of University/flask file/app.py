import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
app =Flask(__name__)
from tensorflow.keras.models import load_model
model =load_model('model.h5')
@app.route('/')
def home():
  return render_template('Demo2.html')
@app.rute('y-predict',method=['post'])
def y_predict():
    min1=[290.0,92.0,1.0,1.0,6.8,0.0]
    max1=[340.0,120.0,5.0,5.0,5.0,9.92,1.0]
    k=[float(x)for x in request.form.values()]
    p=[]
    for i in range(7):
        l=(k[i]-min1[i])/(max1[i]-min1[i])
        p.append(1)
        prediction= model.predict([p])
        print(prediction)
        output=prediction [0]
        if(output==false):
            return render_template('nochance.html',prediction_text='you dont have s chance of getting admisiion');
        else:
            return render_template('chance.html',prediction_text='you  have s chance of getting admisiion');
        if __name__=="__main__":
                 app.run(debug=False)
