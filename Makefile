.PHONY: run
run:
	flask --app main run --host=0.0.0.0

.PHONY: run-https
run-https:
	flask --app main run --host=0.0.0.0 --cert=cert.pem --key=key.pem


.PHONY: lint
lint:
	black .

.PHONY: test
test:
	pytest -v

.PHONY: coverage
coverage:
	coverage report -m

.PHONY: gen-local-cert
gen-local-cert:
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
