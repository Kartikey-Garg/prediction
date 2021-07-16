# -*- coding: utf-8 -*-
import numpy as np
import pickle
from flask import Flask, request, render_template
model = pickle.load(open('C:/Users/Kartikey Garg/Documents/Resources/HIV Dangue All Diseses/Datasets/archive/model.pkl', 'rb')) 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Disease Prediction.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    prediction = model.predict(array_features)
    print(prediction)
    output = prediction
    
    if output == 1:
        return render_template('Disease Prediction.html', 
                               result = 'The patient is not likely to have disease!')
    else:
        return render_template('Disease Prediction.html', 
                               result = 'The patient is likely to have disease!')
if __name__ == '__main__':
    app.run()
