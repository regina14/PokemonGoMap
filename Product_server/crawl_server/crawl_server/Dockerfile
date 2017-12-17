FROM ubuntu:14.04
MAINTAINER Regina

# Level 1
RUN apt-get update -y && apt-get install -y libpq-dev \
                                            python-dev \
                                            ssh\
                                            python-setuptools

RUN easy_install pip

ADD requirements.txt /src/requirements.txt
RUN cd /src; sudo pip install -r requirements.txt

# Copy source code
ADD . /src

RUN mkdir -p /var/log/django

EXPOSE 8000

# run
CMD ["/src/start.sh"]