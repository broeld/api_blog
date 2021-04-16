from django.urls import path

from . import views


urlpatterns = [
    path('', views.CommentList.as_view(),
         name='comment-list-create'),
    path('<int:pk>/', views.CommentDetail.as_view(),
         name='comment-detail'),
    path('<int:comment_id>/replies/', views.RepliesList.as_view())
]
