FROM debian:stretch

RUN LC_ALL=C \
    DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get install -y \
        ca-certificates \
        git \
        python-flask-restful \
        python-ldap \
        python-tornado \
        python-pip \
        && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/*

ADD ./ /opt/app/
WORKDIR /opt/app

EXPOSE 8080

CMD ["python2.7", "server.py"]
