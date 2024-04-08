from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

with open('trained_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate-aqi', methods=['POST'])
def calculate_aqi():
    data = request.json
    pm25i = float(data['pm25'])
    pm10i = float(data['pm10'])
    noi = float(data['no'])
    no2i = float(data['no2'])
    noxi = float(data['nox'])
    nh3i = float(data['nh3'])
    coi = float(data['co'])
    si = float(data['so2'])
    o3i = float(data['o3'])
    benzenei = float(data['benzene'])
    toulenei = float(data['toulene'])
    xylenei = float(data['xylene'])

    # Calculate AQI
    aqi = loaded_model.predict([[o3i, pm10i, noi, nh3i, noxi, xylenei, toulenei, benzenei, coi, pm25i, noxi, si, no2i]])

    return jsonify({'aqi': aqi[0]})

if __name__ == '__main__':
    app.run(debug=True)
