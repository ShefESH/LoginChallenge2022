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
    success = request.args.get("loginSuccessful")
    if success is not None and success == "True":
        return render_template("hacked.html")
    elif success is not None:
        return render_template('home.html', login="True")
    else:
        return render_template('home.html')

@app.route("/verify-login", methods=["POST"])
def verify_login():
    if request.form.get('username') == uname and request.form.get('password') == pwd:
        return redirect("/?loginSuccessful=True")
    else:
        return redirect("/?loginSuccessful=False")