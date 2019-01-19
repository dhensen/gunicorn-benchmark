FROM python:3.7.2-alpine3.8@sha256:f708ad35a86f079e860ecdd05e1da7844fd877b58238e7a9a588b2ca3b1534d8

RUN mkdir /app
WORKDIR /app
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

RUN pip install pipenv
RUN pipenv install --deploy --system

COPY main.py /app/main.py

CMD gunicorn --workers=9 --bind=0.0.0.0:80 main:app
EXPOSE 80
