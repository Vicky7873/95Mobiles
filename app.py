from flask import Flask,render_template
from src.bike.applications.bike import bike_app
from src.car.application.car import car_app
from src.laptop.applications.laptop import laptop_app
from src.mobiles.applications.mobile import mobile_app


app = Flask(__name__)

app.register_blueprint(bike_app, url_prefix='/bike')
app.register_blueprint(car_app, url_prefix='/car')
app.register_blueprint(laptop_app,url_prefix='/laptop')
app.register_blueprint(mobile_app,url_prefix='/mobile')

@app.route('/')
def index():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)