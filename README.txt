########################################################################################################################

                                                      README.txt

########################################################################################################################

# Create new Django project
> django-admin startproject mysite

# Run the Django server
> cd ToProjectDirectory
> python3 manage.py runserver

# Create tables for models in database
> python3 manage.py makemigrations RedPill

# Migrate database
> python3 manage.py migrate

# Create admin user
> python3 manage.py createsuperuser

# install redis
> brew install redis

# run redis server
> brew services start redis
> redis-server

# Run redis at the root of the project
> celery -A RedPill.celery worker -l DEBUG -E

# Stop all process on port
> sudo lsof -t -i tcp:8000 | xargs kill -9

# Regarder le site KELQUARTIER