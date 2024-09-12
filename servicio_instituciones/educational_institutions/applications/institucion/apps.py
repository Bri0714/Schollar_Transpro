from django.apps import AppConfig


# This class is used to configure the application.
# The name attribute is used to identify the application.
class InstitucionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.institucion'
