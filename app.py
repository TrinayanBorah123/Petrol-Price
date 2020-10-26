# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:44:59 2020

@author: Trinayan Borah
"""

from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    features=[float(x) for x in request.form.values()]
    final=[np.array(features)]
    print(features)
    print(final)
    prediction=model.predict(final)
    output='{0:.{1}f}'.format(prediction[0], 2)


    return render_template('Home.html',pred='The price of Petrol in Chennai is nearly Rs.{}/- '.format(output))


if __name__ == '__main__':
    app.run(debug=True)
