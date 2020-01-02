#!/bin/sh

exec gunicorn -b :5000 --workers 2 -k gevent --access-logfile - --error-logfile - autoapp:app
