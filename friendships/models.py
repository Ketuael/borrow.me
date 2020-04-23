from django.db import models
from backend.settings import AUTH_USER_MODEL as User


# Create your models here.


class Friendship(models.Model):
    sender = models.ForeignKey(User, related_name="friendship_initiator", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="friendship_receiver", on_delete=models.CASCADE)

    confirmed = models.BooleanField(default=False)


