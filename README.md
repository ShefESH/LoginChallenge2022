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