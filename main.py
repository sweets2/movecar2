from flask import Flask
from weather_script import get_weather_forecast, check_thunderstorm_forecast

app = Flask(__name__)


@app.route("/")
def hello():
    get_weather_forecast()
    return check_thunderstorm_forecast()
