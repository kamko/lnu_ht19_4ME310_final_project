FROM python:3.8-alpine

COPY server /app/server
COPY requirements.txt docker-entrypoint.sh autoapp.py /app/
WORKDIR /app

RUN apk update \
    && apk add --no-cache --virtual .build-deps gcc musl-dev \
    && apk add --no-cache py3-gevent \
    && pip install gunicorn gevent \
    && apk del .build-deps gcc musl-dev

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "./docker-entrypoint.sh" ]
