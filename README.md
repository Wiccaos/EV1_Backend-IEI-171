CMD:

python -m venv ambiente

pip install django mysqlclient djangorestframework


SQL:

CREATE DATABASE 'ev1-backend';


CMD:

python manage.py migrate

python manage.py createsuperuser
