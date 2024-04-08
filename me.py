from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

app = Flask(__name__)

# Load your dataset and skip the first two columns
df = pd.read_csv("city_day.csv", usecols=lambda column: column not in [0, 1, 15])

# Remove 'City', 'Date', and 'AQI_Bucket' columns
df.drop(columns=['City', 'Date', 'AQI_Bucket'], inplace=True)

# Convert non-numeric columns to numeric
df = df.apply(pd.to_numeric, errors='coerce')

# Drop features with all missing values
df.dropna(axis=1, how='all', inplace=True)

# Replace missing values with the median of each column
imputer = SimpleImputer(strategy='median')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Train your linear regression model
reg = LinearRegression()
reg.fit(df_imputed[['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']], df_imputed['AQI'])

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate-aqi', methods=['POST'])
def calculate_aqi():
    data = request.json
    pm25 = float(data['pm25'])
    pm10 = float(data['pm10'])
    no = float(data['no'])
    no2 = float(data['no2'])
    nox = float(data['nox'])
    nh3 = float(data['nh3'])
    co = float(data['co'])
    so2 = float(data['so2'])
    o3 = float(data['o3'])
    benzene = float(data['benzene'])
    toulene = float(data['toulene'])
    xylene = float(data['xylene'])

    # Calculate AQI
    aqi = reg.predict([[pm25, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toulene, xylene]])

    return jsonify({'aqi': aqi[0]})

if __name__ == '__main__':
    app.run(debug=True)
