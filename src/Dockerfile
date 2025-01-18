FROM python:3.13

LABEL Maintainer="AMIRMALLAEI@Gmail.com"
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

RUN apt-get update -y && apt-get install -y gcc ghostscript
RUN pip install --upgrade pip

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code

RUN pip install -r requirements.txt
ADD . /code