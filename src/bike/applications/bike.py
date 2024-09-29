from flask import Flask,render_template,Blueprint,request
from sklearn.preprocessing import LabelEncoder,StandardScaler
from log import logger
import joblib
import pandas as pd

bike_app  = Blueprint('bike_app',__name__,template_folder='/Users/bhikipallai/Desktop/Projects/95Mobiles/templates')

model = joblib.load("models/tunned_model.pkl")

@bike_app.route('/')
def index():
    return render_template("bike_index.html")

@bike_app.route("/predict",methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        bike_name = request.form['bike_name']
        city = request.form['city']
        kms_driven = float(request.form['kms_driven'])
        owner = request.form['owner']
        age = float(request.form['age'])
        power = float(request.form['power'])
        brand = request.form['brand']

        cat_cols = ['bike_name', 'city', 'owner', 'brand']
        num_cols = ['kms_driven', 'power']

        le = LabelEncoder()
        stc = StandardScaler()

        df = pd.DataFrame({
            "bike_name": [bike_name],
            "city": [city],
            "kms_driven": [kms_driven],
            "owner": [owner],
            "age": [age],
            "power": [power],
            "brand": [brand]
        })

        le = LabelEncoder()
        for col in cat_cols:
            df[col] = le.fit_transform(df[col])

        stc = StandardScaler()
        df[['kms_driven', 'power']] = stc.fit_transform(df[['kms_driven', 'power']])

        result = model.predict(df)

        return render_template("bike_result.html",predicted_price = result)
    