from rest_framework import serializers
from django.contrib.auth import password_validation
from users.models import User
from django.contrib.auth.models import BaseUserManager


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, data):
        password_validation.validate_password(password=data)
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

