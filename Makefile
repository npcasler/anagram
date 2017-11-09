.PHONY: clean-pyc clean-build clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests with default Python"
	@echo "coverage - check code coverage with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "dist - package"
	@echo "install - install the packge to the active Python's site-packages"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.pyo" -exec rm -f {} +
	find . -name "*~" -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .coverage/
	rm -fr htmlcov/

test: 
	nosetests

coverage:
	coverage run --source anagram setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/anagram.rst
	sphinx-apidoc -o docs anagram
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

docs-test:
	python setup.py check --restructuredtext

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py install
