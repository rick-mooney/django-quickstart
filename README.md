## Create a directory on your desktop named develop.  This is a folder where all of your dev work happens

## Create a subdirectory in develop for your new project

## Create a github repo

## Clone the empty repo into your new folder

## Install Django
pipenv install django
To use a specific version of Django use:
pipenv install django==<version_name> <br/>
    example: pipenv install django==2.2.6

## Create a Project
django-admin startproject <project_name> <br/>
    example: django-admin startproject core

## Create an App
django-admin startapp <app_name> <br/>
    example: django-admin startapp example

## Run the environment - pipenv shell

## Run the App
python manage.py makemigrations <br/>
python manage.py migrate <br/>
python manage.py runserver <br/>

## Create a django admin user
python manage.py createsuperuser

## Update settings.py
Template URLs to use subfolders <br/>
add GA_TAG parameter

## Create .env variables

## Connect to a postgres database
1. In PGADMIN, Connect to a server and create a new user for a new database you will create
2. Create a new database and make your new user the owner of the database
3. In settings.py, update the DATABASE attributes 
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASS',''),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}``` 
The NAME variable must match the name of the database you made.
## Create base html file
Create file views.py <br/>
Create templates folder in core<br/>
update urls.py to include the base file<br/>
  This will actually need to be update after creating the first app though.  Its just setup now to verify the install
