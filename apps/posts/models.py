from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    creation_date = models.DateField(auto_now=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    user_upvotes = models.ManyToManyField(User,
                                          related_name="posts_upvoted",
                                          blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="posts")

    class Meta:
        ordering = ("-creation_date",)

    def __str__(self):
        return self.title
