from rest_framework import serializers
from friendships.models import Friendship
from users.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from backend.settings import MEDIA_ROOT


class FriendshipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['id', 'sender', 'receiver', 'confirmed']


class FriendshipDetailSerializer(serializers.ModelSerializer):

    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    class Meta:
        model = Friendship
        fields = ['id', 'sender', 'receiver', 'confirmed']

    def get_sender(self, obj):
        user = obj.sender
        sender = [user.id, user.email, user.first_name, user.last_name]
        return sender

    def get_receiver(self, obj):
        user = obj.receiver
        receiver = [user.id, user.email, user.first_name, user.last_name]
        return receiver


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



