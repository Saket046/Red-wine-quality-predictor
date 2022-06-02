from flask import Flask,request, url_for, redirect, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model=pickle.load(open('wine_quality_model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    if (request.method == 'POST'):
        Fixed_Acidity=request.form['Fixed Acidity']
        Volatile_Acidity=request.form['Volatile Acidity']
        Citric_Acid=request.form['Citric Acid']
        Residual_Sugar=request.form['sugar']
        Chlorides=request.form['clorides']
        Free_Sulfur_Dioxide=request.form['sulfur dioxide']
        Total_Sulfur_Dioxide=request.form['Total sulfur dioxide']
        Density=request.form['Density']
        pH=request.form['pH']
        Sulphates=request.form['Sulphates']
        Alcohol=request.form['alcohol']
    try:
        data=[[float(Fixed_Acidity),float(Volatile_Acidity),float(Citric_Acid),float(Residual_Sugar),float(Chlorides),float(Free_Sulfur_Dioxide),float(Total_Sulfur_Dioxide),float(Density),float(pH),float(Sulphates),float(Alcohol)]]
        inputdf = pd.DataFrame(data, columns=['fixed acidity', 'volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol'])
        prediction=model.predict(inputdf)
        output=prediction[0]
        
        if output==0:
            return render_template('index.html',pred='Result : Your wine quality is Poor. \n',bhai="mat piyo")
        else:
            return render_template('index.html',pred='Result : Your wine quality is Great. \n',bhai="pilo bhai")
    except:
        return render_template('index.html',pred='Make sure you fill all the values correctly. \n',bhai="")


if __name__ == '__main__':
    app.run(debug=True)
