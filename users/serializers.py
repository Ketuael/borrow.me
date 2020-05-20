from rest_framework import serializers
from django.contrib.auth import password_validation
from users.models import User
from friendships.models import Friendship
from transactions.models import MoneyTransaction


def get_balance(self, obj):
    user = self.context['request'].user
    friend = obj

    given = 0
    taken = 0

    for transaction in MoneyTransaction.objects.all():
        if transaction.giver == user and transaction.taker == friend:
            given += transaction.ammount
        elif transaction.giver == friend and transaction.taker == user:
            taken += transaction.ammount

    balance = given - taken

    return {"given": given, "taken": taken, "total_balance": balance}


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
                balance = get_balance(self, friend.receiver)
                friend_list.append([user.data, friend.confirmed, friend.id, balance])
            else:
                user = UserListSerializer(friend.sender)
                balance = get_balance(self, friend.sender)
                friend_list.append([user.data, friend.confirmed, friend.id, balance])

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


