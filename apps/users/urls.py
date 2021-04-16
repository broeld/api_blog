from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserCreate.as_view(), name="user-create"),
    path("<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
]
