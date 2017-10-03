# Blog

>Based Python2.7 Django-1.11.1

>UI based emlog model Life

> __Author__ = Moon3r

## Modify Database infomation in blogs/setting.py
Like this:
```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'Database_Name',
            'USER': 'Datebase_Username',
            'PASSWORD': 'Database_Password',
            'HOST': 'Database_Ip',
            'PORT': 'Database_Port',
        }
    }
```
