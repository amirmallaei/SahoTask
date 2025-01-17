#!/usr/bin/env bash

python3 manage.py makemigrations Tracking &&

python3 manage.py migrate &&

# python3 manage.py runserver 182.29.100.45:8081
gunicorn saho.wsgi -c ./Deployment/gunicorn/gunicorn.py -b 182.29.100.45:8081
