from django.apps import AppConfig
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this function
    def ready(self):
        from . import signals

