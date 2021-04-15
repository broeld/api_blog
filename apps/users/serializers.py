from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 8}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        user = User.objects.get(username=instance.username)
        password = validated_data.get('password', instance.password)
        username = validated_data.get('username', instance.username)

        user.username = username
        user.set_password(password)

        user.save()

        return user
