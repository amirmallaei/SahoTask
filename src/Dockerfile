FROM python:3.9

LABEL Maintainer="AMIRMALLAEI@Gmail.com"
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update -y && apt-get install -y gcc ghostscript libc-dev tzdata 

RUN pip install --upgrade pip setuptools wheel

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code

RUN pip install -r requirements.txt
ADD . /code