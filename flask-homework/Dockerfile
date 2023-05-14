FROM python:3.11

WORKDIR /data

COPY requirements.txt .

RUN pip install -r reqiurements.txt

COPY . .

EXPOSE 4200

CMD flask run 0.0.0.0:4200
