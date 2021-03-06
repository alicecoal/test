FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_USER=appuser


RUN groupadd -r ${APP_USER} -g 1000 && useradd --no-log-init --create-home -u 1000 -r -g ${APP_USER} ${APP_USER}

ARG APP_DIR=/home/${APP_USER}/project/
RUN echo $APP_DIR && mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}

COPY ./requirements.txt ${APP_DIR}

RUN set -ex &&\
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ${APP_DIR}requirements.txt

RUN apt-get -q update && \
    apt-get -qy install postgresql-client \
                        musl-dev \
                        gcc \
                        netcat \
                        gettext \
                        libgettextpo-dev \
                        libjpeg-dev \
                        xmlsec1 && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=${APP_USER}:${APP_USER} ishop ${APP_DIR}

USER ${APP_USER}:${APP_USER}

WORKDIR ${APP_DIR}
