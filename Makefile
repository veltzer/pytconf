.PHONY: all
all:
	pytest --cov=pytconf --cov-report=xml --cov-report=html
	pylint pytconf tests
	pyflakes pytconf tests
	flake8 pytconf tests

.PHONY: test
test:
	pytest --cov=pytconf --cov-report=xml --cov-report=html

.PHONY: flake8
flake8:
	flake8 pytconf tests


.PHONY: pyflakes
pyflakes:
	pyflakes pytconf tests

.PHONY: pylint
pylint:
	pylint pytconf tests
