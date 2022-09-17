from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request
from flask_bootstrap import Bootstrap

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from numpy import identity

app = Flask(__name__)
Bootstrap(app)

# no need for sqlite authentication, just store uname/password
#add alternative option to guess easy creds
uname = "admin"
pwd = "password"

app.config["JWT_SECRET_KEY"] = ";nod87b;/dfub6vaz.knib"
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

jwt = JWTManager(app)

@app.route("/")
def index():
    success = request.args.get("loginSuccessful")
    if success is not None and success == "True":
        return render_template("hacked.html")
    elif success is not None:
        return render_template('home.html', login="Failed")
    else:
        return render_template('home.html')

@app.route("/verify-login", methods=["POST"])
def verify_login():
    if request.form.get('username') == uname and request.form.get('password') == pwd:
        return redirect("/?loginSuccessful=True")
    else:
        return redirect("/?loginSuccessful=False")

@app.route("/hard")
def hard():
    id_dict = {'is_admin': False}
    access_token = create_access_token(identity=id_dict)
    resp = make_response(redirect("/cookie-jar"))
    resp.set_cookie('access_token_cookie', access_token)
    return resp

@app.route("/cookie-jar")
@jwt_required()
def cookie_jar():
    identity = get_jwt_identity()
    if identity['is_admin']:
        return render_template("cookie-jar.html", allowed=True)
    else:
        return render_template("cookie-jar.html", allowed=False)