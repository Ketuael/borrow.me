from rest_framework import serializers
from datetime import date
from users.serializers import UserListSerializer
from transactions.models import Transaction, MoneyTransaction


class TransactionsListSerializer(serializers.ModelSerializer):
    giver = serializers.SerializerMethodField()
    taker = serializers.SerializerMethodField()
    user_is_giver = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'user_is_giver', 'giver', 'taker', 'name', 'description', 'pub_date', 'due_date', 'status']

    def get_giver(self, obj):
        return UserListSerializer(obj.giver).data

    def get_taker(self, obj):
        return UserListSerializer(obj.taker).data

    def get_user_is_giver(self, obj):
        if obj.giver == self.context['request'].user:
            return True
        else:
            return False


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction

        fields = ['giver', 'taker', 'name', 'description', 'due_date']

    def create(self, validated_data):
        giver = validated_data['giver']
        taker = validated_data['taker']

        due_date = validated_data['due_date']

        if giver == taker:
            raise serializers.ValidationError('You already own this item, silly!')
        if date.today() >= due_date:
            raise serializers.ValidationError('You can\'t lend item for the past!')

        transaction = Transaction.objects.create(**validated_data)
        transaction.save()
        return transaction


class UpdateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'description', 'due_date', 'status']

    # item - monetary divider


class MoneyTransactionsListSerializer(serializers.ModelSerializer):

    friend = serializers.SerializerMethodField()
    ammount = serializers.SerializerMethodField()

    class Meta:
        model = MoneyTransaction
        fields = ['id', 'friend', 'ammount']

    def get_friend(self, obj):
        user = self.context['request'].user

        if obj.giver == user:
            return UserListSerializer(obj.taker).data
        else:
            return UserListSerializer(obj.giver).data

    def get_ammount(self, obj):
        if obj.giver == self.context['request'].user:
            return obj.ammount
        else:
            return (-1)*obj.ammount


class CreateMoneyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyTransaction
        fields = ['giver', 'taker', 'ammount']

    def create(self, validated_data):
        giver = validated_data['giver']
        taker = validated_data['taker']

        if giver == taker:
            raise serializers.ValidationError('You can\'t lend money to yourself... do you?')

        transaction = MoneyTransaction.objects.create(**validated_data)
        transaction.save()
        return transaction


