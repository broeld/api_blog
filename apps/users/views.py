from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import UserSerializer
from .permissions import IsUser


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
