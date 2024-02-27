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

## Move from sqlite to Postgres

- install postgres dependencies

```sh
cd django
pip3 install psycopg2-binary
```

- Dump datas

```sh
python manage.py dumpdata posts > datadump.json
```

- Update .env

```sh
POSTGRES_PASSWORD=django_secret
POSTGRES_USER=django_user
POSTGRES_DB=django_db
```

- Add docker-compose

```yml
version: "3.9"

services:
  postgres:
    image: postgres:14-alpine
    ports:
      - 5432:5432
    volumes:
      - postgres_db:/var/lib/postgresql/data
    env_file:
      - .env

volumes:
  postgres_db:
    driver: local
```

- Launch postgres with Docker Compose

```sh
docker-compose -d up
```

- Update app/settings.py :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- load datas

```sh
python manage.py loaddata datadump.json
```
