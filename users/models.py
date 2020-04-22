from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/avatars/{1}'.format(instance.id, filename)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, avatar=None, password=None):
        if not email:
            raise ValueError('Musisz podac adres email')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, avatar=None)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    is_anonymous = False
    is_authenticated = True

    def get_friends(self):
        friends = Friendship.objects.filter(active=True, sender=self).filter(active=True, revicer=self)
        return friends


class Friendship(models.Model):
    sender = models.ForeignKey(User, related_name="friendship_initiator", on_delete=models.CASCADE)
    reciver = models.ForeignKey(User, related_name="friendship_reciver", on_delete=models.CASCADE)

    active = models.BooleanField(default=False)
