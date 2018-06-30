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

test:
	coverage run --branch --source=django/  django/./manage.py test django/ -v 2
	coverage report --omit=django/*/migrations*,django/patient_schedules/settings/*,django/patient_schedules/urls.py,django/patient_schedules/wsgi.py,django/manage.py,django//*/tests/*,django//__init__.py

# dev commands

runserver: clean
	$(DJANGO_CMD) runserver 0.0.0.0:8000 --settings=$(SETTINGS)

# load test commands

artillery:
	artillery run artillery.yml
