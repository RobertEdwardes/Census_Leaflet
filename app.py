from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        CENSUS_API = f'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={address}&benchmark=2020&format=json'
        census_json = requests.get(CENSUS_API)
        if census_json.status_code != 200:
            return f'<h1>JSON request went wrong got {census_json.status_code}</h1>'
        return census_json.json()
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()