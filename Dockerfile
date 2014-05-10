FROM ubuntu:14.04
MAINTAINER devops@mayflower.de

RUN apt-get update; apt-get -y upgrade

RUN apt-get -y install python-virtualenv python-dev puppet

RUN apt-get clean

ADD . /srv/geordi

RUN cd /srv/geordi;\
    virtualenv .;\
    bin/pip install -r requirements.txt

EXPOSE 5000

CMD ["/srv/geordi/bin/python", "/srv/geordi/app.py"]
