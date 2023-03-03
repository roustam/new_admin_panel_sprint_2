FROM nginx:1.19.2

ARG nginx_uid=33
ARG nginx_gid=33

RUN usermod -u $nginx_uid -o nginx && groupmod -g $nginx_gid -o nginx

RUN mkdir -p /var/www/static