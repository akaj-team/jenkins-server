FROM jenkinsci/blueocean

USER root

RUN apk update \
    && apk upgrade \
    && apk add maven \
    && apk add python3 \
    && apk add --no-cache tzdata

RUN mkdir /root/scripts
ENV PATH="/root/scripts:${PATH}"
#ENV TZ=Asia/Ho_Chi_Minh

COPY plugins.txt /plugins.txt
RUN /usr/local/bin/install-plugins.sh < /plugins.txt

