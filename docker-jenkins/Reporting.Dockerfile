# at/reporting
FROM ruby:2.6.1-alpine3.8
USER root

RUN mkdir -p vendor/bundle
RUN apk add libgcrypt-dev make gcc libc-dev git
RUN gem install bundle --no-document -- --use-system-libraries