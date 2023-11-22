FROM mysql:8.2.0

# This is the dev database - credentials will be changed for production
ENV MYSQL_ROOT_PASSWORD=password

ENV MYSQL_DATABASE=LinkShortener
ENV MYSQL_USER=link
ENV MYSQL_PASSWORD=password

EXPOSE 3306
COPY init.sql /docker-entrypoint-initdb.d/
