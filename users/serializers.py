from rest_framework import serializers
from django.contrib.auth import password_validation
from users.models import User
from friendships.models import Friendship


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']


class UserDetailSerializer(serializers.ModelSerializer):

    friends = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar', 'friends']

    def get_friends(self, obj):
        friends1 = Friendship.objects.filter(sender=obj)
        friends2 = Friendship.objects.filter(receiver=obj)
        friends = friends1.union(friends2)

        friend_list = []
        for friend in friends:
            if friend.sender == obj:
                user = UserListSerializer(friend.receiver)
                friend_list.append([user.data, friend.confirmed])
            else:
                user = UserListSerializer(friend.sender)
                friend_list.append([user.data, friend.confirmed])

        return friend_list


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


