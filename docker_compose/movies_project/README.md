Для запуска проекта выполните команду docker-compose up в директории с файлом docker-compose.yml.

websrv_movies - nginx
backend_movies - django
postgres_movies - База данных

Для статического контента в docker-compose.yml создан volume "static-files".

После сборки образов и запуска контейнеров необходимо выполнить миграции и сборку статики.
Это все делается в контейнере backend_movies. Сервис uwsgi запускается под пользователем web.

Миграции - python manage.py migrate
Сбор статики - python manage.py collectstatic

В контейнере backend_movies используется bash скрипт entrypoint.sh , в нем определен путь к uwsgi.
Сначала я добавил туда выполнение миграций и сбор статики, но потом в общем чате рекомендовали убрать.

