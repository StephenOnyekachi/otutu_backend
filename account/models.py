

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    status = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

