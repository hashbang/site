FROM python:3-alpine
MAINTAINER Hashbang Team <team@hashbang.sh>

ADD ./ /opt/app/
WORKDIR /opt/app

EXPOSE 8080

CMD ["python2.7", "server.py"]
