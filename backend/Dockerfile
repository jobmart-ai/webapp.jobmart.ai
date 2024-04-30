FROM ubuntu:latest

RUN apt-get update && apt-get install -y mysql-server
RUN apt-get update && apt-get install -y libmysqlclient-dev
RUN apt-get update && apt-get install -y poppler-utils

RUN apt-get update && apt-get install -y python3 python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN python --version && pip --version

RUN apt-get update && apt-get install -y python3-venv
ENV PATH="/venv/bin:$PATH"

RUN apt-get update && apt-get install -y pkg-config

RUN python -m venv /venv
SHELL ["/bin/bash", "-c"]
RUN source /venv/bin/activate

RUN /venv/bin/pip install pdf2image
RUN /venv/bin/pip install django

RUN export MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
RUN export MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"
RUN /venv/bin/pip install mysqlclient

WORKDIR /backend
COPY . .

EXPOSE 8000
CMD ["sh", "-c", "ls && \
    python runtime_services/manage.py makemigrations && \
    python runtime_services/manage.py migrate && \
    python runtime_services/manage.py runserver 0.0.0.0:8000"]