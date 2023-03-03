FROM python:3.10

WORKDIR /opt/app

COPY uwsgi.ini uwsgi.ini
COPY config/wsgi.py wsgi.py
COPY requirements.txt requirements.txt
COPY movies movies
COPY config config
COPY manage.py manage.py
COPY entrypoint.sh entrypoint.sh
RUN ["chmod", "+x", "/opt/app/entrypoint.sh"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'
ENV DEBUG ${DEBUG}
ENV IP_ADDRESSES ${IP_ADDRESSES}
ENV SECRET_KEY SECRET_KEY${DJANGO_SETTINGS_MODULE}

RUN groupadd -r web && useradd -d /opt/app -r -g web web \
    && chown web:web -R /opt/app \
    && apt-get -y update && apt-get -y install gettext

USER web

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && mkdir static && mkdir static_root

EXPOSE 8000


ENTRYPOINT ["sh", "/opt/app/entrypoint.sh"] 