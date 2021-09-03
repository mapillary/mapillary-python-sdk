# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)

define PYTHON_SCRIPT

import os
import sys

sys.path.insert(0, os.path.abspath('../'))


def skip(app, what, name, obj, would_skip, options):
    '''Skip'''

    extensions.append('sphinx_autodoc_typehints')

    if name in ('__init__',):
        return False
    return would_skip


    def setup(app):
        '''Setup App'''

        app.connect('autodoc-skip-member', skip)
endef

# SETUP

# # Setup all
setup: setup-prod setup-dev

# # Install needed dependencies
setup-prod:
	python -m pip install --upgrade pip
	pip install pipenv
	pipenv install

# # Install developer dependencies
setup-dev:
	python -m pip install --upgrade pip
	pip install pipenv
	pipenv install --dev

# PACKAGE BUILD

# # Build the package
build:
	# Builds the package distributions
	python3 setup.py sdist bdist_wheel --universal

local-install:
	# Locally install mapillary - DO THIS ONLY AFTER RUNNING `make build`
	pip3 install -e .

# CODE QUALITY

# # Styling related
style: format lint

# # # Formatting
format:
	@ black src/mapillary

# # # Linting
lint:
	@ # stop the build if there are Python syntax errors or undefined names
	@ flake8 src/mapillary --count --select=E9,F63,F7,F82 --show-source --statistics

	@ # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	@ flake8 src/mapillary --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# DOCUMENTATION

# # For generating the latest developer documentation from src/mapillary
# # and serving them locally with Docusaurus
docs-gen: docs-sphinx docs-py docs-start

# # # Sphinx Documentation Generation
docs-sphinx:
	sphinx-apidoc -o sphinx-docs ./src/ sphinx-apidoc --full -A 'Mapillary'; cd sphinx-docs; echo "$$PYTHON_SCRIPT" >> conf.py; make markdown;

# # # Python Script for moving markdown from sphinx -> docusaurus
docs-py:
	python3 scripts/documentation.py

# # # Serve the newly generated documentation
docs-start:
	cd docs; npm run start;

# # For pushing the docs to the gh-pages branch
docs-push: docs-build docs-deploy

# # # Building the static pages
docs-build:
	# Building the documentation
	cd docs; npm run build;

# # # Deploying the documentation to gh-pages
docs-deploy:
	# Deploying the documentation
	# Deploying requires GIT_USER's password and write access to the repository
	# If normal password authentication is used, deployment fails
	# remote: Support for password authentication was removed on August 13, 2021.
	# Please use a personal access token instead. See here for more information
	# https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/
	cd docs; GIT_USER=Rubix982 yarn deploy;

# CLEANING

# # Removing temporary created artifacts
clean: sphinx-docs-clean docs-clean build-clean

# # # Remove Sphinx Documentation
sphinx-docs-clean:
	rm -rf sphinx-docs/

# # # Remove latest build of docs
docs-clean:
	rm -rf docs/build

# # # Remove latest sr/mapillary build
build-clean:
	rm -rf build/ dist/

# TESTING

# # Execute pytest on tests/
test:
	@ pytest --log-cli-level=20
