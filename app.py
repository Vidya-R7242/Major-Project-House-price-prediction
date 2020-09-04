#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import os
#import processing as fl
get_ipython().system('pip install processing')

app = Flask(__name__) #Initialize the flask App
#model = pickle.load(open('model.pkl', 'rb'))
print(os.getcwd())
model = pickle.load(open('C:/Users/Administrator/Desktop/CAPSTONE/model/housePrice.pkl', 'rb'))  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    
    int_features = [(str(x) + "-" + request.form.get(x)) for x in request.form.keys()]
    final_features = [np.array(int_features)]
    '''
    
    cols = ['cid', 'dayhours', 'room_bed', 'room_bath', 'living_measure',
       'lot_measure', 'ceil', 'coast', 'sight', 'condition', 'quality',
       'ceil_measure', 'basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long', 'living_measure15', 'lot_measure15', 'furnished',
       'total_area']
    df = pd.DataFrame()
    a=[]
    for col in cols:
        a.append(request.form.get(col))
        print("cols = {} {}".format(str(col),request.form.get(col)))
        df[col]= request.form.get(col)
    print(a)  
    final_features = a
    render_template('index.html', prediction_text='Calculating House Price........')
    fl.data_preprocessing(final_features)
    
    
    '''
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    '''    
    output = np.round(fl.predictPrice(),2)
    

    return render_template('index.html', prediction_text='House Price should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




