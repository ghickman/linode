SHELL := /bin/bash

release:
	rm -rf dist/*
	python setup.py register bdist_wheel sdist
	twine upload dist/*

test:
	py.test
