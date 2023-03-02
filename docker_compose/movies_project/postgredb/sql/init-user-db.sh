#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER app;
	CREATE DATABASE movies_database;
	GRANT ALL PRIVILEGES ON DATABASE movies_database TO app;
EOSQL