FROM python:3.11

WORKDIR /data

COPY requirements.txt .

RUN pip install -r reqiurements.txt

COPY . .

EXPOSE 8000

CMD python manage.py runsever 0.0.0.0:8000