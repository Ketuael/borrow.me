from datetime import datetime
from django.db import models
from users.models import User


# Create your models here.


class Transaction(models.Model):
    giver = models.ForeignKey(User, related_name="item_giver", on_delete=models.CASCADE)
    taker = models.ForeignKey(User, related_name="item_taker", on_delete=models.CASCADE)
    #sender_is_giver = models.BooleanField(blank=False, default=True)
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)
    pub_date = models.DateField(default=datetime.now)
    due_date = models.DateField()
    status = models.CharField(max_length=50, blank=False, default='not_confirmed')
    #photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)


class MoneyTransaction(models.Model):
    giver = models.ForeignKey(User, related_name="money_giver", on_delete=models.CASCADE)
    taker = models.ForeignKey(User, related_name="money_taker", on_delete=models.CASCADE)
    #sender_is_giver = models.BooleanField(blank=False, default=True)
    ammount = models.IntegerField(blank=False, default=0)