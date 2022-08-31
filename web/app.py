from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# no need for sqlite authentication, just store uname/password
uname = "SESHAdmin"
pwd = "You#Still]Won't[Guess\This!2022,"

@app.route("/")
def index():
    hacked = request.args.get("DIDYOUHACKIT")
    if hacked is not None and hacked == "TRUE":
        return render_template("hacked.html")
    elif hacked is not None:
        return render_template('home.html', hacked="NOPE")
    else:
        return render_template('home.html')

@app.route("/verify-login", methods=["POST"])
def verify_login():
    if request.form.get('username') == uname and request.form.get('password') == pwd:
        return redirect("/?DIDYOUHACKIT=TRUE")
    else:
        return redirect("/?DIDYOUHACKIT=FALSE")