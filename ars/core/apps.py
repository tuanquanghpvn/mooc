from django.apps import AppConfig

class UsersAppConfig(AppConfig):
    name = 'ars.core'
    verbose_name = "User's Profile"

    def ready(self):
        from ars.core import signals
