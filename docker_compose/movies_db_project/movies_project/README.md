Для запуска проекта выполните команду docker-compose up в директории с файлом docker-compose.yml.

Имена контейнеров:

websrv_movies - nginx
backend_movies - django
postgres_movies - База данных

Для статического контента в docker-compose.yml создан volume "static-files".

После сборки образов и запуска контейнеров необходимо выполнить миграции и сборку статики.
Это все делается в контейнере backend_movies. Сервис uwsgi запускается под пользователем web.

Зайти в контейнер можно командой docker exec -it backend_movies bash

Миграции - python manage.py migrate --noinput
Сбор статических файлов - python manage.py collectstatic
Создание переводов - python manage.py compilemessages -l en -l ru 

Создание учетной записи администратора python manage.py createsuperuser --username admin
Далее, скрипт попросит ввести email(можно оставить пустым) и пароль.

