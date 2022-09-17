from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request, session, render_template_string
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

app.secret_key = "pinrg8gns#arjg;/-]]"

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

@app.route("/hungry")
def hungry():
    id_dict = {'is_admin': False}
    access_token = create_access_token(identity=id_dict)
    resp = make_response(render_template("hungry.html"))
    resp.set_cookie('access_token_cookie', access_token)
    return resp

@app.route("/who-are-you", methods=["POST"])
def get_name():
    tmp = request.form.get('name')
    if len(tmp) > 12:
        return render_template("hungry.html", fail=True)
    else:
        session['name'] = tmp
        return redirect("/cookie-jar")

@app.route("/cookie-jar")
@jwt_required()
def cookie_jar():
    identity = get_jwt_identity()
    name = session['name']

    if identity['is_admin']:
        welcome = "Congratulations! You win a laptop sticker!"
        return render_template("cookie-jar.html", welcome_msg=welcome, win=True)
    else:
        msg = "Hello " + name + "! Unfortunately, only admins are allowed to open the cookie jar."
        welcome = render_template_string(msg)
        return render_template("cookie-jar.html", welcome_msg=welcome)

@app.route("/cleanup")
def cleanup():
    """clear cookies and any temp variables"""
    session['name'] = None
    resp = make_response(redirect('/'))
    resp.set_cookie('access_token_cookie', '', expires=0)
    resp.set_cookie('Authorization', '', expires=0)
    return resp