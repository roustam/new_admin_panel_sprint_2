FROM postgres:15

ENV POSTGRES_USER=$DB_USER
ENV POSTGRES_PASSWORD=$DB_PASSWORD
ENV POSTGRES_DB=$DB_NAME

# COPY sql/init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh