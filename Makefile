PROJECT_NAME = fundtracker
SHELL := /bin/sh
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  all                      to setup the whole development environment for the project"
	@echo "  virtualenv               to create the virtualenv for the project"
	@echo "  requirements             install the requirements to the virtualenv"
	@echo "  db                       create the PostgreSQL db for the project"
	@echo "  migrate                  run the migrations"
	@echo "  serve                	  Start the django dev server"
	@echo "  superuser                Create superuser with name superuser and password pass"

.PHONY: requirements


all: virtualenv requirements db migrate runserver

# Command variables
MANAGE_CMD = python manage.py
PIP_INSTALL_CMD = pip install
VIRTUALENV_NAME = djangios

# Helper functions to display messagse
ECHO_BLUE = @echo "\033[33;34m $1\033[0m"
ECHO_RED = @echo "\033[33;31m $1\033[0m"

# The default server host local development
HOST ?= localhost:8000
DEPLOY_ENV = production

virtualenv: 
	virtualenv $(VIRTUALENV_NAME)

requirements:
	( \
		workon $(virutalenv) \
		$(PIP_INSTALL_CMD) -r requirements/local.txt; \
	)

db:
	createdb $(PROJECT_NAME)

migrations:
	( \
	    $(MANAGE_CMD) makemigrations; \
	)


migrate:
	( \
		$(MANAGE_CMD) migrate; \
	)

serve:
	( \
		$(MANAGE_CMD) runserver $(HOST); \
	)

superuser:
	( \
		echo "from django.contrib.auth.models import User; User.objects.create_superuser('superuser', 'superuser@example.com', 'pass')" | ./manage.py shell; \
	)

clean:
# Remove all *.pyc, .DS_Store and temp files from the project
	$(call ECHO_BLUE,removing .pyc files...)
	@find . -name '*.pyc' -exec rm -f {} \;
	$(call ECHO_BLUE,removing static files...)
	@rm -rf $(PROJECT_NAME)/_static/
	$(call ECHO_BLUE,removing temp files...)
	@rm -rf $(PROJECT_NAME)/_tmp/
	$(call ECHO_BLUE,removing .DS_Store files...)
	@find . -name '.DS_Store' -exec rm {} \;

shell:
# Run a local shell for debugging
	( \
		$(MANAGE_CMD) shell; \
	)
