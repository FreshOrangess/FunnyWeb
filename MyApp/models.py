from django.db import models


# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class qq_kongjian(models.Model):
    qq = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class messages(models.Model):
    username = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

