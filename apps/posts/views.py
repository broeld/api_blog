from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpvoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = self.request.user
        if post in user.posts_upvoted.all():
            post.user_upvotes.remove(user)
        else:
            post.user_upvotes.add(user)

        post.amount_of_upvotes = post.user_upvotes.count()
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data)
