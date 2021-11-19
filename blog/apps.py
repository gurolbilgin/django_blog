from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

# this is for signals.py file otherwise it is also write codes in models file too
    def ready(self):
        import blog.signals
