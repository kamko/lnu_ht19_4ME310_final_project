FROM python:3.8.1-slim-buster

COPY server /app/server
COPY requirements.txt docker-entrypoint.sh autoapp.py /app/
WORKDIR /app

RUN pip install gunicorn
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "./docker-entrypoint.sh" ]
