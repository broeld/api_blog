from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    amount_of_upvotes = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "title",
                  "link", "creation_date",
                  "amount_of_upvotes", "author"]

    def get_amount_of_upvotes(self, obj):
        return obj.user_upvotes.count()
