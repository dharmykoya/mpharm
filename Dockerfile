# pull official base image
FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /mpharm
WORKDIR /mpharm

COPY . /mpharm/
RUN pip install --no-cache-dir -r requirements.txt

