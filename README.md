# blog-webapp-django
A Django project where we can create, read, update and delete the blog posts. Also we can register the newsletters, and able to see the recent posts, comments and a page navigator to shift the pages.

First clone the repository from Github and switch to the new directory:

$ git clone git@github.com/USERNAME/<project_name>.git

$ cd <project_name>

Setup the project structure:
```
-sample (project folder)
        -src
              -sample (project name)
                      -sample (main app name)
                              -settings.py
                              -urls.py
                              -wsgi.py
                       -app1
                       -app2
                       -appn
                       -requirements.txt
                       -manage.py      
        -venv  
```
Activate the virtualenv for your project.

PROJECT CONFIGURATION if first time
========================================
install virtualenv first
```
pip install --user virtualenv 
```
create virtual environment named venv
```
python -m virtualenv venv
```
activate the venv using activate script
```
venv\Scripts\activate
```
install django in the same venv
```
pip install django
```
to see the installed packages
```
pip freeze
```
install the driver for interacting with PostgreSQL from the Python scripting language
```
pip install psycopg2
```
install postgres for the first time or use sqlite by default
```
depends on the OS

 setup postgres sql
 setup server, username, password, port no. etc
 create database
```
Install project dependencies:
```
$ pip install -r requirements/local.txt
```
Then simply apply the migrations:
```
$ python manage.py migrate
```
You can now run the development server:
```
$ python manage.py runserver
```

1. Home Page

  ![main page ](https://github.com/thedevsafaf/blog-webapp-django/assets/85129653/07bd64f8-8b9d-450a-8adc-5bde704bb353)

2. Page Navigator and NewsLetter

  ![page navigator and newsletter](https://github.com/thedevsafaf/blog-webapp-django/assets/85129653/b3923ad7-7d49-4385-8c0f-be536780fa02)

3. Recent Posts

   ![recent posts](https://github.com/thedevsafaf/blog-webapp-django/assets/85129653/607e6ad3-e799-4bba-bbe8-9ddf5ebccd64)

4. Admin Page
    
  ![admin page](https://github.com/thedevsafaf/blog-webapp-django/assets/85129653/91915f55-3516-497b-a4c7-0b838fc49d2f)



