from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.methods == 'POST':
        return 
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()