FROM python:2-alpine
MAINTAINER Hashbang Team <team@hashbang.sh>

ADD ./ /opt/app/
WORKDIR /opt/app

RUN apk add py2-flask

EXPOSE 8080

CMD ["python2.7", "server.py"]
