from apscheduler.schedulers.background import BackgroundScheduler

from . models import Post


def reset_post_upvotes():
    posts = Post.objects.all()
    for post in posts:
        post.user_upvotes.clear()
        post.amount_of_upvotes = post.user_upvotes.count()
        post.save()


def start_reset_post_upvotes():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reset_post_upvotes, 'cron', minute=1, hour=0)
    scheduler.start()
