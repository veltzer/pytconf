.PHONY: all
all:
	pytest --cov=pytconf --cov-report=xml --cov-report=html
	pylint pytconf tests
	pyflakes pytconf tests
	flake8 pytconf tests

.PHONY: pytest
pytest:
	pytest --cov=pytconf --cov-report=xml --cov-report=html

.PHONY: unittest
unittest:
	python -m unittest

.PHONY: flake8
flake8:
	flake8 pytconf tests


.PHONY: pyflakes
pyflakes:
	pyflakes pytconf tests

.PHONY: pylint
pylint:
	pylint pytconf tests
