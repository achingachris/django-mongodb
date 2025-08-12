# Django Meets NoSQL BREAKING UP WITH RELATIONSHIPS, BUT KEEPING THE ORM

## Demo Project: Django Login, Logout, Signup, Password Change, and Password Reset
REF: https://learndjango.com/tutorials/django-login-and-logout-tutorial


Installation: pip install --pre django-mongodb-backend

Until the package is out of beta, you must use pip’s --pre option

Link: https://django-mongodb-backend.readthedocs.io/en/latest/intro/install/

Requirements

```txt
asgiref==3.9.1
Django==5.2.5
django-mongodb-backend==5.2.0b1
dnspython==2.7.0
pymongo==4.14.0
sqlparse==0.5.3
```

django-admin startproject config . --template https://github.com/mongodb-labs/django-mongodb-project/archive/refs/heads/5.2.x.zip

local connection string: mongodb://localhost:27017/


database settings:

```python
# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": django_mongodb_backend.parse_uri("mongodb://localhost:27017/djangoconafricademo"),
}

# Database routers
# https://docs.djangoproject.com/en/dev/ref/settings/#database-routers
DATABASE_ROUTERS = ["django_mongodb_backend.routers.MongoRouter"]
```

Account URLS:

```txt
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
```

