from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Comment


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source="author.username")
    replies = ReadOnlyField()
    post = ReadOnlyField(source="post.id")
    parent = ReadOnlyField(source="parent.id", required=False)

    class Meta:
        model = Comment
        fields = ["id", "author", "content", "creation_date",
                  "post", "replies", "parent"]
