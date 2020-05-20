
from django.test import TestCase
from rest_framework import serializers, generics

from transaction.models import Transaction
from users.models import User
# Create your tests here.


class TransactionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'giver', 'taker', 'name', 'description', 'pub_date', 'due_date', 'status']





class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction

        fields = ['id', 'giver', 'taker', 'name', 'description', 'due_date', 'status']

        def validate(self, data):
            """
            Check that start is before finish.
            """
            if data['pub_date'] > data['due_date']:
                raise serializers.ValidationError("finish must occur after start")
            return data


class UpdateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'description', 'due_date', 'status']


class RemoveTransactionSerializer(generics.RetrieveDestroyAPIView):
    class Meta:
        model = Transaction
        fields = ['id', 'giver', 'taker', 'name', 'description', 'due_date', 'status']


class ConfirmTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['giver', 'taker', 'status']
        extra_kwargs = {'sender': {'read_only': True}, 'receiver': {'read_only': True}}

        def update(self, instance, validated_data):
            instance.status = validated_data['status']
            instance.save()
            return instance
