FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev libpq-dev
RUN apk del .tmp-build-deps


# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


# Setup directory structure
RUN mkdir /app
RUN chown -R $(whoami):$(whoami) app/
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user