# React Vite / Django

```sh
mkdir projet
cd project
python3 -m venv venv
source venv/bin/activate
pip3 install django django-cors-headers django-environ
django-admin startproject app
mv app django
cd  django/
pip3 freeze > requirement.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp posts
cd..
code .
```

## Configure env file

```sh
cd django
touch .env
```

## Update app/settings.py :

```sh
import environ
env = environ.Env()
environ.Env.read_env(env_file='./.env')
```
