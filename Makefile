DJANGO_CMD = python3 django/manage.py
SETTINGS = patient_schedules.settings

# management commands

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

requirements-pip:
	@pip install --upgrade pip
	@pip install -r requirements.txt

migrations:
	$(DJANGO_CMD) makemigrations

migrate:
	$(DJANGO_CMD) migrate

createsuperuser:
	$(DJANGO_CMD) createsuperuser

collectstatic:
	$(DJANGO_CMD) collectstatic --noinput

compress:
	$(DJANGO_CMD) compress

shell:
	$(DJANGO_CMD) shell

install: requirements-pip migrate createsuperuser
	@echo "Installation completed"

# test commands


# dev commands

runserver: clean
	$(DJANGO_CMD) runserver 0.0.0.0:8000 --settings=$(SETTINGS)
