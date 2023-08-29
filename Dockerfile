FROM alpine:latest

RUN apk add --update --no-cache python3 poetry && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip

COPY . /app

WORKDIR /app/web

RUN poetry install

CMD poetry run flask run -h 0.0.0.0 -p 5000
