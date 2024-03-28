Deploying our app to Heroku

Check that heroku is installed:
```
heroku --version
```
If it's not installed, follow this: https://devcenter.heroku.com/articles/heroku-cli

Install the followings:
```
pip install --no-dependencies django-heroku
pip install gunicorn dj_database_url python-decouple psycopg2-binary whitenoise
```

Create Procfile in the project directory and add the following line:
```
web: gunicorn <name_of_app>.wsgi # from django-admin startproject command
```
If you're uncertain of the project name, look at the wsgi.py file ('project_name.settings')

Back to the terminal
```
pip freeze > requirements.txt
```

In settings.py
```
import django_heroku
import dj_database_url
from decouple import config

# For static files
import os

MIDDLEWARE = [
	'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
```

Make sure you have already created a repo on Github, then push
```
git add .
git commit -m 'commit'
git push
```

Make sure you already have an ssh key created, but if you haven't, deactivate venv and then:
```
mkdir ~/.ssh
cd ~/.ssh
ssh-keygen
```

Then go back to the terminal and go back to the app directory
```
heroku login
heroku keys:add
heroku create
heroku rename <CHANGEME> # this is optional
git push heroku master
```
