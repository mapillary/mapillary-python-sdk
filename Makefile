# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)

define PYTHON_SCRIPT
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

def skip(app, what, name, obj,would_skip, options):
	if name in ( '__init__',):
		return False
	return would_skip

	def setup(app):
		app.connect('autodoc-skip-member', skip)
	extensions.append('sphinx_autodoc_typehints')
endef

style: format lint

format:
	black src/mapillary

lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 src/mapillary --count --select=E9,F63,F7,F82 --show-source --statistics

	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 src/mapillary --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

sphinx-docs:
	sphinx-apidoc -o sphinx-docs ./src/ sphinx-apidoc --full -A 'Mapillary'; cd sphinx-docs; echo "$$PYTHON_SCRIPT" >> conf.py; make markdown;

sphinx-docs-clean:
	rm -rf sphinx-docs/

docs: docs-build docs-deploy

docs-deploy:
	# Deploying the documentation
	# Deploying requires GIT_USER's password and write access to the repository
	# If normal password authentication is used, deployment fails
	# remote: Support for password authentication was removed on August 13, 2021.
	# Please use a personal access token instead. See here for more information
	# https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/
	cd docs; GIT_USER=Rubix982 yarn deploy;

docs-build:
	# Building the documentation
	cd docs; npm run build;

docs-clean:
	rm -rf docs/build

test:
	@ pytest --log-cli-level=20

clean: sphinx-docs-clean docs-clean