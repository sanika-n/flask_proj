from flask import Flask, render_template, request
from waitress import serve
import requests

app=Flask(__name__)

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/uploader", methods=["POST"] )
def uploader():
    f=request.files['xyz']
    f.save(f.filename)
    return "File Uploaded Successfully"
@app.route("/")
def home():
    api_key = 'CWxaqdXM0SyM60LpZhvnebyhgyt2hBApVwb5hcS6'
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    return render_template("home.html", data=data.body)


    
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)