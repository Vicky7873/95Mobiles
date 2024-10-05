from flask import Flask,render_template,Blueprint,request
from sklearn.preprocessing import StandardScaler,LabelEncoder
from log import logger
import joblib
import pandas as pd

laptop_app = Blueprint('laptop_app',__name__,template_folder="/Users/bhikipallai/Desktop/Projects/95Mobiles/templates")
model = joblib.load("models/laptop_model.pkl")

le = LabelEncoder()
stc = StandardScaler()

@laptop_app.route('/')
def index():
    return render_template("laptop_index.html")

@laptop_app.route('/predict',methods = ["GET","POST"])
def predict():
    if request.method == "POST":
        Company = request.form["company"]
        Product = request.form["product"]
        typename = request.form['typename']
        inches = float(request.form['inches'])
        screen_resolution = request.form['screen_resolution']
        cpu = request.form['cpu']
        ram = request.form['ram']
        memory = request.form['memory']
        gpu = request.form['gpu']
        opsys = request.form['opsys']
        weight = float(request.form['weight'])


        df = pd.DataFrame({
            "Company":[Company],
            "Product": [Product],
            "TypeName": [typename],
            "Inches": [inches],
            "ScreenResolution":[screen_resolution],
            "Cpu":[cpu],
            "Ram":[ram],
            "Memory":[memory],
            "Gpu":[gpu],
            "OpSys": [opsys],
            "Weight":[weight]
        })

        cat_cols = []
        num_cols = []

        for col in df.columns:
            if df[col].dtype == 'float64':
                num_cols.append(col)
            elif df[col].dtype == 'object':
                cat_cols.append(col)
                

        for col in df[num_cols]:
            df[col] = stc.fit_transform(df[[col]])
        
        for col in df[cat_cols]:
            df[col] = le.fit_transform(df[col])
        
        result = model.predict(df)

    return render_template("laptop_result.html",predicted_price = result)

