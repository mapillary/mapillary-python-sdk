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

style:
	black src/mapillary && flake8 src/mapillary

docs:
	sphinx-apidoc -o docs ./src/ sphinx-apidoc --full -A 'Mapillary'; cd docs; echo "$$PYTHON_SCRIPT" >> conf.py; make markdown;

docs-clean:
	rm -rf docs/