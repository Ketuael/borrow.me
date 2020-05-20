from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from users.serializers import UserListSerializer
from friendships.models import Friendship
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

    def validate(self, data):
        giver = data['giver']
        taker = data['taker']
        due_date = data['due_date']

        if giver == taker:
            raise serializers.ValidationError('You already own this item, silly!')
        if date.today() >= due_date:
            raise serializers.ValidationError('You can\'t lend item for the past!')

        is_friend = False
        try:
            Friendship.objects.get(sender=giver, receiver=taker, confirmed=True)
            is_friend = True
        except ObjectDoesNotExist:
            pass
        try:
            Friendship.objects.get(sender=giver, receiver=taker, confirmed=True)
            is_friend = True
        except ObjectDoesNotExist:
            pass

        if not is_friend:
            raise serializers.ValidationError('You aren\'t friend of this User, so you can\'t create transaction with him')

        return data


class UpdateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'description', 'due_date', 'status']

    # item - monetary divider

    def validate(self, data):
        due_date = data['due_date']
        status = data['status']

        if date.today() >= due_date:
            raise serializers.ValidationError('You can\'t lend item for the past!')
        if status != "not_confirmed":
            raise serializers.ValidationError('This is unchangeable dummy field, don\'t touch it :).')

        return data


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

    def validate_ammount(self, value):
        if value <= 0:
            raise serializers.ValidationError("You must give/take positive ammount of money.")
        return value

    def validate(self, data):
        giver = data['giver']
        taker = data['taker']

        if giver == taker:
            raise serializers.ValidationError('You can\'t lend money to yourself... do you?')
        is_friend = False

        try:
            Friendship.objects.get(sender=giver, receiver=taker, confirmed=True)
            is_friend = True
        except ObjectDoesNotExist:
            pass
        try:
            Friendship.objects.get(sender=giver, receiver=taker, confirmed=True)
            is_friend = True
        except ObjectDoesNotExist:
            pass

        if not is_friend:
            raise serializers.ValidationError('You aren\'t friend of this User, so you can\'t create transaction with him')

        return data


