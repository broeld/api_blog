from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.posts"

    def ready(self):
        from .recurring_job import start_reset_post_upvotes

        start_reset_post_upvotes()
