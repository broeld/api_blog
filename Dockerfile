FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /news_api

COPY requirements.txt /news_api/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /news_api/
