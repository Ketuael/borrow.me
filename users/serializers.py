from rest_framework import serializers
from django.contrib.auth import password_validation
from users.models import User, Friendship


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, data):
        password_validation.validate_password(password=data)
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, data):
        password_validation.validate_password(password=data)
        return data

    def update(self, instance, validated_data):
        user = super(UpdateUserSerializer, self).update(instance, validated_data)
        if "password" in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['id', 'sender', 'reciver', 'active']


