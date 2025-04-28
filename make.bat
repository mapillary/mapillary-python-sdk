@echo off


IF /I "%1"=="def skip(app, what, name, obj, would_skip, options)" GOTO def skip(app, what, name, obj, would_skip, options)
IF /I "%1"=="    if name in ('__init__',)" GOTO     if name in ('__init__',)
IF /I "%1"=="    def setup(app)" GOTO     def setup(app)
IF /I "%1"=="setup" GOTO setup
IF /I "%1"=="setup-prod" GOTO setup-prod
IF /I "%1"=="setup-dev" GOTO setup-dev
IF /I "%1"=="build" GOTO build
IF /I "%1"=="local-install" GOTO local-install
IF /I "%1"=="style" GOTO style
IF /I "%1"=="format" GOTO format
IF /I "%1"=="lint" GOTO lint
IF /I "%1"=="docs-gen" GOTO docs-gen
IF /I "%1"=="docs-sphinx" GOTO docs-sphinx
IF /I "%1"=="docs-py" GOTO docs-py
IF /I "%1"=="docs-start" GOTO docs-start
IF /I "%1"=="docs-push" GOTO docs-push
IF /I "%1"=="docs-build" GOTO docs-build
IF /I "%1"=="docs-deploy" GOTO docs-deploy
IF /I "%1"=="clean" GOTO clean
IF /I "%1"=="sphinx-docs-clean" GOTO sphinx-docs-clean
IF /I "%1"=="docs-clean" GOTO docs-clean
IF /I "%1"=="build-clean" GOTO build-clean
IF /I "%1"=="dump-clean" GOTO dump-clean
IF /I "%1"=="test" GOTO test
IF /I "%1"=="test-no-warn" GOTO test-no-warn
GOTO error

:def skip(app, what, name, obj, would_skip, options)
	'''Skip'''
	GOTO :EOF

:    if name in ('__init__',)
	return False
	return would_skip
	GOTO :EOF

:    def setup(app)
	'''Setup App'''
	GOTO :EOF

:setup
	CALL make.bat setup-prod
	CALL make.bat setup-dev
	GOTO :EOF

:setup-prod
	python -m pip install --upgrade pip
	pip install pipenv
	pipenv install
	GOTO :EOF

:setup-dev
	python -m pip install --upgrade pip
	pip install pipenv
	pipenv install --dev
	GOTO :EOF

:build
	pipenv run python3 -m build
	GOTO :EOF

:local-install
	pipenv run pip install -e .
	GOTO :EOF

:style
	CALL make.bat format
	CALL make.bat lint
	GOTO :EOF

:format
	@ black src/mapillary
	@ black tests/
	GOTO :EOF

:lint
	@
	@ flake8 src/mapillary --count --select=E9,F63,F7,F82 --show-source --statistics
	@ flake8 tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
	GOTO :EOF

:docs-gen
	CALL make.bat docs-sphinx
	CALL make.bat docs-py
	CALL make.bat docs-start
	GOTO :EOF

:docs-sphinx
	sphinx-apidoc -o sphinx-docs ./src/ sphinx-apidoc --full -A 'Mapillary'; cd sphinx-docs; echo "$$PYTHON_SCRIPT" >> conf.py; make markdown;
	GOTO :EOF

:docs-py
	python3 scripts/documentation.py
	GOTO :EOF

:docs-start
	PUSHD docs; npm run start; && POPD
	GOTO :EOF

:docs-push
	CALL make.bat docs-build
	CALL make.bat docs-deploy
	GOTO :EOF

:docs-build
	PUSHD docs; npm run build; && POPD
	GOTO :EOF

:docs-deploy
	PUSHD docs; GIT_USER=Rubix982 yarn deploy; && POPD
	GOTO :EOF

:clean
	CALL make.bat sphinx-docs-clean
	CALL make.bat docs-clean
	CALL make.bat build-clean
	CALL make.bat dump-clean
	GOTO :EOF

:sphinx-docs-clean
	DEL /Q sphinx-docs/ -rf
	GOTO :EOF

:docs-clean
	DEL /Q docs/build -rf
	GOTO :EOF

:build-clean
	DEL /Q build/ dist/ -rf
	GOTO :EOF

:dump-clean
	DEL /Q tests/dump/ -rf
	GOTO :EOF

:test
	@ pytest --log-cli-level=20
	GOTO :EOF

:test-no-warn
	@ pytest --log-cli-level=20 --disable-warnings
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
