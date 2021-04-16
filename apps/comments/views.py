from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from apps.posts.models import Post
from apps.posts.permissions import IsAuthorOrReadOnly

from .models import Comment
from .serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def get_post(self):
        post_id = self.kwargs.get("post_id")
        if post_id is None:
            raise NotFound()

        post = get_object_or_404(Post, id=post_id)
        return post

    def get_queryset(self):
        post = self.get_post()
        comments = Comment.objects.filter(post=post)
        return comments

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        if post_id is None:
            raise NotFound()

        post = get_object_or_404(Post, id=post_id)

        comments = Comment.objects.filter(post=post)
        return comments


class RepliesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def get_post(self):
        post_id = self.kwargs.get("post_id")

        if post_id is None:
            raise NotFound()

        post = get_object_or_404(Post, id=post_id)
        return post

    def get_comment(self):
        comment_id = self.kwargs.get("comment_id")

        if comment_id is None:
            raise NotFound()

        parent = get_object_or_404(Comment, id=comment_id)
        return parent

    def get_queryset(self):
        post = self.get_post()
        parent = self.get_comment()

        comments = Comment.objects.filter(post=post, parent=parent)
        return comments

    def perform_create(self, serializer):
        post = self.get_post()
        parent = self.get_comment()

        serializer.save(author=self.request.user, post=post, parent=parent)
