IMG ?= my-lmdeploy-dev
MODEL ?= qween

build:
	docker buildx build -f Dockerfile -t $(IMG) .

fresh:
	docker buildx build -f Dockerfile -t $(IMG) . --no-cache

up:
	docker compose up -d

down:
	docker compose down

log:
	docker compose logs --tail=100 -f

restart:
	$(MAKE) down
	$(MAKE) up
	$(MAKE) log

in:
	docker compose exec lmdeploy bash

ps:
	docker compose ps

status:
	curl -X GET http://localhost:9030/status \
	-H "Content-Type: application/json" 

switch:
	curl -X POST http://localhost:9030/model \
	-H "Content-Type: application/json" \
	-d '{"model": "$(MODEL)"}'

model:
	curl -X GET http://localhost:9030/model \
	-H "Content-Type: application/json"
