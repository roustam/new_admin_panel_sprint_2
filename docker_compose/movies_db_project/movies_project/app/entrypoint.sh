#!/bin/bash

# python manage.py migrate
# python manage.py collectstatic

export PATH=/opt/app/.local/bin:$PATH
uwsgi --strict --ini /opt/app/uwsgi.ini