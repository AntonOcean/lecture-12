.PHONY: run
run:
	flask --app main run

.PHONY: lint
lint:
	black .

.PHONY: test
test:
	pytest -v

.PHONY: coverage
coverage:
	coverage report -m


