from django.db import models
from users.models import User, user_directory_path


# Create your models here.

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name="transaction_initiator", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="transaction_receiver", on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=50, blank=False)
    opis = models.CharField(max_length=200, blank=False)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateTimeField('due date')
    status = models.CharField(max_length=50, blank=False)
    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)


class TransactionMoney(models.Model):
    sender = models.ForeignKey(User, related_name="transaction_initiator", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="transaction_receiver", on_delete=models.CASCADE)
    balance = models.CharField(max_length=10, blank=False)
