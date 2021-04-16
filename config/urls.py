from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("news_api_admin/", admin.site.urls),
    path("api/users/", include("apps.users.urls")),
    path("api/posts/", include("apps.posts.urls")),
]
