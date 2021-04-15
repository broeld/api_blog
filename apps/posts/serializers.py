from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Post


class PostSerializer(ModelSerializer):
    amount_of_upvotes = ReadOnlyField()
    author = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'link', 'creation_date',
                  'amount_of_upvotes', 'author']
