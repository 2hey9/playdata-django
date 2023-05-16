from django.apps import AppConfig

class CalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cal'

class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'
