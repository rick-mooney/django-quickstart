# Create a directory on your desktop named develop.  This is a folder where all of your dev work happens

# Create a subdirectory in develop for your new project

# Create a github repo

# Clone the empty repo into your new folder

# Install Django
pipenv install django
To use a specific version of Django use:
pipenv install django==<version_name>
    example: pipenv install django==2.2.6

# Create a Project
django-admin startproject <project_name>
    example: django-admin startproject core

# Create an App
django-admin startapp <app_name>
    example: django-admin startapp example

# Run the environment - pipenv shell

# Run the App
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Create a django admin user
python manage.py createsuperuser

# Update settings.py
Template URLs to use subfolders
add GA_TAG parameter

# Create .env variables

# Connect to a postgres database

# Create base html file
Create file views.py
Create templates folder in core
update urls.py to include the base file
  This will actually need to be update after creating the first app though.  Its just setup now to verify the install
