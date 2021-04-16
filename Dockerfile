FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY _u5r)d0=voq(kxwubnhko_$$*elh+x(xs28g=@ljc7^4c0z$$r%m

WORKDIR /news_api

COPY requirements.txt /news_api/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /news_api/

RUN  python manage.py collectstatic --noinput
