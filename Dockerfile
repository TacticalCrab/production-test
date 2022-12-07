FROM python:3.10.5-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /flaskr

COPY ./flaskr .

CMD [ "python3", "-m", "gunicorn", "-w", "2", "-b", "0.0.0.0", "app:app" ]