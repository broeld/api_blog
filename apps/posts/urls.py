from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.PostListCreate.as_view(), name="post-list-create"),
    path("<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path(
        "<int:post_id>/upvote/", views.UpvoteView.as_view(), name="post-upvote"
    ),
    path("<int:post_id>/comments/", include("apps.comments.urls")),
]
