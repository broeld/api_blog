from django.db import models
from django.contrib.auth.models import User
from apps.posts.models import Post


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    post = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField()
    creation_date = models.DateField(auto_now=True)

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='replies',
                               blank=True)

    class Meta:
        ordering = ('creation_date',)

    def __str__(self):
        return self.content
