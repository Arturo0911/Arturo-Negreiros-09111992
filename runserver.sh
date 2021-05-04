#!/bin/bash

pipenv shell

pipenv install -r requirements.txt

python Travel_agency/manage.py runserver
