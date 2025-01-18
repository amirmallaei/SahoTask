#!/usr/bin/env bash
python3 manage.py makemigrations Tracking &&python3 manage.py migrate && #python3 manage.py runserver 0.0.0.0:8081
gunicorn saho.wsgi -c ./Deployment/gunicorn/gunicorn.py -b 192.168.1.100:8081
