from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = "apps.posts"

    def ready(self):
        from .recurring_job import start_reset_post_upvotes

        start_reset_post_upvotes()
