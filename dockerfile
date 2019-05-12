FROM python:3.7

ENV PYTHONUNBUFFERED 1

# COPY ./server /server
COPY ./back/requirements /back/requirements

WORKDIR /back

RUN pip install -r requirements/prod.txt