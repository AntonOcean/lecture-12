.PHONY: run
run:
	flask --app main run --host=0.0.0.0

.PHONY: lint
lint:
	black .

.PHONY: test
test:
	pytest -v

.PHONY: coverage
coverage:
	coverage report -m


