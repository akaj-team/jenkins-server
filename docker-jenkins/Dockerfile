FROM jenkinsci/blueocean

USER root

RUN apk update \
    && apk upgrade \
    && apk add maven \
    && apk add python3

RUN mkdir /root/scripts
ENV PATH="/root/scripts:${PATH}"

COPY plugins.txt /plugins.txt
RUN /usr/local/bin/plugins.sh /plugins.txt

