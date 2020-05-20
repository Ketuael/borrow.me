from datetime import datetime

from django.db import models
from users.models import User, user_directory_path


# Create your models here.

class Transaction(models.Model):
    giver = models.ForeignKey(User, related_name="item_giver", on_delete=models.CASCADE)
    taker = models.ForeignKey(User, related_name="item_taker", on_delete=models.CASCADE)
    #sender_is_giver = models.BooleanField(blank=False, default=True)
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=False)
    pub_date = models.DateField('date published', default=datetime.now)
    due_date = models.DateField('due date')
    status = models.CharField(max_length=50, blank=False, default='not_confirmed')
    #photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)


class Money(models.Model):
    giver = models.ForeignKey(User, related_name="money_giver", on_delete=models.CASCADE)
    taker = models.ForeignKey(User, related_name="money_taker", on_delete=models.CASCADE)
    ammount = models.FloatField(max_length=10, blank=False, default=0)


