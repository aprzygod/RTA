FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt app.py perceptron.pickle ./
RUN pip install -r requirements.txt

ENV FLASK_APP=app

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]