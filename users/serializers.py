from rest_framework import serializers
from django.contrib.auth import password_validation
from users.models import User, Friend


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


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['user', 'friends']


class AddFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields=['friends']

    def update(self, instance, validated_data):
        friends = super(AddFriendSerializer, self).update(instance, validated_data)
        #for user in validated_data['friends']:
            #Friend.objects.get(user=user).save
        return friends