# Dockerfile for Real-Time Route Tracking Microservice
FROM python:3

COPY . /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8007"]
