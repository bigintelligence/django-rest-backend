FROM python:3
ENV PYTHONUNBUFFERED 1

ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_SECRET_KEY
ARG DB_ENGINE
ARG PG_DRIVER
ARG PG_USER
ARG PG_PASS
ARG PG_HOST
ARG PG_PORT
ARG PG_BASE

ENV DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV DB_ENGINE $DB_ENGINE
ENV PG_DRIVER $PG_DRIVER
ENV PG_USER $PG_USER
ENV PG_PASS $PG_PASS
ENV PG_HOST $PG_HOST
ENV PG_PORT $PG_PORT
ENV PG_BASE $PG_BASE
# to install Geospatial libraries
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y binutils libproj-dev gdal-bin && rm -rf /var/lib/apt/lists/*

RUN mkdir /djangorestbackend
WORKDIR /djangorestbackend
COPY requirements.txt /djangorestbackend/
COPY wait-for-postgres.sh /djangorestbackend/
COPY pgconnectcheck.py /djangorestbackend/
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /djangorestbackend/