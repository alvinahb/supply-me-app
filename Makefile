postgres:
	docker run --name postgres15 -p 5432:5432 -e POSTGRES_DB=supply-me-test -e POSTGRES_USER=root -e POSTGRES_PASSWORD=supply-me-2024 -d postgres:15-alpine

createdb:
	docker exec -it postgres15 createdb --username=root --owner=root supply-me-test

dropdb:
	docker exec -it postgres15 dropdb supply-me-test

migrations:
	python manage.py makemigrations supplyme

migrate:
	python manage.py migrate

sqlmigrate:
	python manage.py sqlmigrate supplyme 0001

test:
	python manage.py test ./supplyme/tests

server:
	python manage.py runserver

.PHONY: postgres createdb dropdb migrate migrations sqlmigrate server
