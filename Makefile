install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.wh

lint:
	poetry run flake8

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml