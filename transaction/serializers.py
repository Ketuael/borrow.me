from rest_framework import serializers
from datetime import date
from transaction.models import Transaction


class TransactionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'giver', 'taker', 'name', 'description', 'pub_date', 'due_date', 'status']


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction

        fields = ['giver', 'taker', 'name', 'description', 'due_date']

    def create(self, validated_data):
        giver = validated_data['giver']
        taker = validated_data['taker']

        due_date = validated_data['due_date']

        if giver == taker:
            raise serializers.ValidationError('Sender is the same as receiver!')
        if date.today() >= due_date:
            raise serializers.ValidationError('You can\'t lend item for the past!')

        transaction = Transaction.objects.create(**validated_data)
        transaction.save()
        return transaction


class UpdateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'description', 'due_date', 'status']
