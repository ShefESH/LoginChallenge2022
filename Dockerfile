FROM fedora:latest

COPY . /loginchallenge

WORKDIR /loginchallenge

RUN python3 -m venv loginchallenge_venv

RUN loginchallenge_venv/bin/pip install -r requirements.txt

CMD loginchallenge_venv/bin/python3 -m flask --app web/app.py run -h 0.0.0.0 -p 1234
