from apscheduler.schedulers.background import BackgroundScheduler

from .models import Post


def reset_post_upvotes():
    posts = Post.objects.all()
    for post in posts:
        post.user_upvotes.clear()
        post.save()


def start_reset_post_upvotes():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reset_post_upvotes, "cron", minute=5, hour=0)
    scheduler.start()
