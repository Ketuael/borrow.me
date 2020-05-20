from rest_framework import serializers
from users.serializers import UserListSerializer
from friendships.models import Friendship
from transactions.models import MoneyTransaction
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class FriendshipListSerializer(serializers.ModelSerializer):

    friend = serializers.SerializerMethodField()
    has_to_accept = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Friendship
        fields = ['id', 'confirmed', 'has_to_accept', 'friend', 'balance']

    def get_friend(self, obj):
        user = self.context['request'].user
        if obj.sender == user:
            return UserListSerializer(obj.receiver).data
        else:
            return UserListSerializer(obj.sender).data

    def get_has_to_accept(self, obj):
        user = self.context['request'].user
        if obj.receiver == user and not obj.confirmed:
            return True
        else:
            return False

    def get_balance(self, obj):
        user = self.context['request'].user
        friend = self.get_friend(obj)

        given = 0
        taken = 0

        for transaction in MoneyTransaction.objects.all():
            if transaction.giver == user and transaction.taker.id == friend["id"]:
                given += transaction.ammount
            elif transaction.giver.id == friend["id"] and transaction.taker == user:
                taken += transaction.ammount

        balance = given - taken

        return {"given":given, "taken":taken, "total_balance":balance}


class FriendshipDetailSerializer(serializers.ModelSerializer):

    friend = serializers.SerializerMethodField()

    class Meta:
        model = Friendship
        fields = ['id', 'friend']

    def get_friend(self, obj):
        user = self.context['request'].user
        if obj.sender == user:
            return UserListSerializer(obj.receiver).data
        else:
            return UserListSerializer(obj.sender).data


class AddFriendSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Friendship
        fields = ['id', 'sender', 'receiver']

    def create(self, validated_data):
        sender = validated_data['sender']
        receiver = validated_data['receiver']

        if sender == receiver:
            raise ValidationError('Sender is the same as receiver!')
        else:
            try:
                Friendship.objects.get(sender=sender, receiver=receiver)
                raise ValidationError('This friendship already exists!')
            except ObjectDoesNotExist:
                pass

            try:
                Friendship.objects.get(sender=receiver, receiver=sender)
                raise ValidationError('This friendship already exists!')
            except ObjectDoesNotExist:
                pass

        friendship = Friendship.objects.create(**validated_data)
        friendship.save()
        return friendship


class ConfirmFriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['id', 'sender', 'receiver', 'confirmed']
        extra_kwargs = {'sender': {'read_only': True}, 'receiver': {'read_only': True}}

    def update(self, instance, validated_data):
        instance.confirmed = validated_data['confirmed']
        instance.save()
        return instance


class RemoveFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['id', 'sender', 'receiver', 'confirmed']



