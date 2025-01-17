from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Item_Weight =float(request.form['Item_Weight'])
            Item_Fat_Content =int(request.form['Item_Fat_Content'])
            Item_Visibility =float(request.form['Item_Visibility'])
            Item_Type =int(request.form['Item_Type'])
            Item_MRP =float(request.form['Item_MRP'])
            Outlet_Establishment_Year =int(request.form['Outlet_Establishment_Year'])
            Outlet_Size =int(request.form['Outlet_Size'])
            Outlet_Location_Type =int(request.form['Outlet_Location_Type'])
            Outlet_Type =int(request.form['Outlet_Type'])
            Years_Established =int(request.form['Years_Established'])
                   
         
            data = [Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type,Years_Established]
            data = np.array(data).reshape(1, 10)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)