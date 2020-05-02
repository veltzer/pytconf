.PHONY: all

all:
	pytest --cov=pytconf --cov-report=xml --cov-report=html
	pylint pytconf tests
	pyflakes pytconf tests
	flake8 pytconf tests
