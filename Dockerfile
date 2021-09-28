# syntax=docker/dockerfile:1
FROM python:3.9.5-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV API_KEY=your_api_key

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]