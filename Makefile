.PHONY: up down build install-producer run-producer run-consumer

up:
	docker-compose up -d

down:
	docker-compose down

build:
	pip install -r requirements.txt

install-producer:
	pip install kafka-python

run-producer:
	python producer.py

run-consumer:
	python consumer.py
