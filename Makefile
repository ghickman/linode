SHELL := /bin/bash

release:
	python setup.py register sdist upload

test:
	nosetests --with-spec

