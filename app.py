from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        CENSUS_API = f'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={address}&benchmark=2020&format=json'
        census_json = requests.get(CENSUS_API)
        data=census_json.json()
        addressMatches = data['result']['addressMatches']
        if len(addressMatches) == 0:
            return f'<h1> No matches for input {address} </h1>'
        addressMatches = addressMatches[0]
        if census_json.status_code != 200:
            return f'<h1>JSON request went wrong <br> got {census_json.status_code}</h1>'
        return render_template('index.html', data=addressMatches)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()