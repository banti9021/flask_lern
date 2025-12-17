from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")
@app.route("/submit",methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("username")
    if username=="sager123"and password=="pass":
         return render_template('welcome html',name=username)



if __name__ == "__main__":
    app.run(debug=True)
