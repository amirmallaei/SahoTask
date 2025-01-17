FROM python:3.13

LABEL Maintainer="AMIRMALLAEI@Gmail.com"
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

RUN mkdir /src
COPY ./src /src
WORKDIR /src/
RUN apt-get update
# Setup GDAL
RUN apt-get update &&\ 
    apt-get install -y --fix-missing binutils libproj-dev 

WORKDIR /src
ADD /src/requirements.txt /src/requirements.txt 

RUN pip install -r requirements.txt 
