from flask import Flask, render_template, request
from waitress import serve

app=Flask(__name__)

@app.route("/")
def upload():
    return render_template("home.html")

@app.route("/uploader", methods=["POST"] )
def uploader():
    f=request.files['xyz']
    f.save(f.filename)
    return "File Uploaded Successfully"

    
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)