install:
	$(info ************  Not command ************)
install-requirements:
	pipenv sync
install-requirements-dev:
	pipenv sync --dev
pep8:
	pipenv run flake8 .
formatter:
	pipenv run black . -S -v --py36 --exclude .venv -l 99 
	make pep8
coverage:
	coverage xml	 
	python-codacy-coverage -r coverage.xml
clean:
	pipenv --rm
test:
	pipenv run py.test --cov=apps --cov-config .coveragerc
	coverage html