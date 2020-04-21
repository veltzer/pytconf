.PHONY: all

all:
	pylint -E pytconf
	pyflakes pytconf
	pytest
