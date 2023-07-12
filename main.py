from flask import Flask, request, render_template, jsonify
from weather_script import Weather

app = Flask(__name__)


@app.route("/")
def home():
    instance = Weather()
    return instance.check_thunderstorm_forecast()


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'GET':
        result = request.form
        return render_template("get_location.html", result = result)
    elif request.method == 'POST':
        data = request.get_json()
        latitude = data.get('latitude')
        return render_template("get_location.html", data = data)
#        longitude = data.get('longitude')
#        return f'Latitude: {latitude}, Longitude: {longitude}'
        #return jsonify({'status': 'success'}), 200


@app.route('/location', methods=['POST', 'GET'])
def location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print(f'Latitude: {latitude}, Longitude: {longitude}')
    return {'status': 'success'}, 200
