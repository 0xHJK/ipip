.PHONY: test

dev:
	pip install setuptools pytest black twine flake8

ci:
	py.test --junitxml=report.xml

test:
	python3 setup.py test
	pytest

coverage:
	py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=ipip --junitxml=report.xml tests

flake8:
	black .
	flake8 --ignore=E501,F401,W503 ipip

clean:
	rm -fr build dist .egg ipip.egg-info
	rm -fr .pytest_cache coverage.xml report.xml htmlcov
	find . | grep __pycache__ | xargs rm -fr
	find . | grep .pyc | xargs rm -f
	pip uninstall ipip
	
install:
	python3 setup.py install

publish:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
