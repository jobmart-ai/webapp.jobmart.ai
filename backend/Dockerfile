FROM python:3.9-alpine
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apk update
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    git bash

# RUN apt-get update && apt-get install -y mysql-server
# RUN apt-get update && apt-get install -y libmysqlclient-dev
# RUN apt-get update && apt-get install -y poppler-utils

# RUN apt-get update && apt-get install -y python3 python3-pip
# RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN python --version && pip --version

# RUN apt-get update && apt-get install -y python3-venv
# ENV PATH="/venv/bin:$PATH"

# RUN apt-get update && apt-get install -y pkg-config

# RUN python -m venv /venv
# SHELL ["/bin/bash", "-c"]
# RUN source /venv/bin/activate

RUN pip install pdf2image
RUN pip install django

# RUN export MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
# RUN export MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"
# RUN /venv/bin/pip install mysqlclient
RUN pip install djangorestframework
RUN pip install psycopg2

WORKDIR /backend
COPY . .

EXPOSE 8000
CMD ["sh", "-c", "ls && \
    python runtime_services/manage.py makemigrations && \
    python runtime_services/manage.py migrate && \
    python runtime_services/manage.py runserver 0.0.0.0:8000"]