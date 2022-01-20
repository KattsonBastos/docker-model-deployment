FROM python:3.7-slim

RUN apt-get update && apt-get install -y  libgomp1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY API /API

WORKDIR /API

EXPOSE 8001

CMD [ "python3", "app.py" ]