from flask import Flask, render_template
from flask import request
import pandas as pd 
import numpy as np 
from sklearn.externals import joblib


app = Flask(__name__)

#@app.route('/test')
#def test():
#    return "Flask being called for development"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods= ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            NewYork = float(request.form['NewYork'])
            California = float(request.form['California'])
            Florida = float(request.form['Florida'])
            RnD_Spend = float(request.form['RnD_Spend'])
            Admin_Spend = float(request.form['Admin_Spend'])
            Market_Spend = float(request.form['Market_Spend'])
            
            pred_args = [NewYork, California, Florida, RnD_Spend, Admin_Spend, Market_Spend]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1, -1)
            #mul_reg = open("C:\\Users\\anurag.mishra\\OneDrive - Epicor\\Desktop\\Flask_App\\mulitple_linear_model.pkl", 'rb')
            #ml_model = joblib.load(mul_reg)
            model_predict = ml_model.predict(pred_args_arr)
            model_predict = round(float(model_predict), 2)
        
        except ValueError:
            return "Please check if values are entered correctly"
        
    
    return render_template('predict.html', prediction = model_predict)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
	