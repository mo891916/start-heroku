from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Greeting(models.Model):
    my_time = models.DateTimeField("date created", auto_now_add=True)


