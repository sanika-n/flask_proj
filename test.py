from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def upload():
    return render_template("home.html")

@app.route("/uploader", methods=["POST"] )
def uploader():
    f=request.files['xyz']
    f.save(f.filename)
    return "File Uploaded Successfully"

    
if (__name__=="__main__"):
    app.run(debug=True)