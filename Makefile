#  Makefile

install:
	@poetry install

lint:
	poetry run flake8 brain_game

.PHONY: install lint
