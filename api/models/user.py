from django.db import models


class User(models.Model):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    user_pass = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=12)
    address = models.TextField(max_length=100)
    address_2 = models.TextField(max_length=100, null=True, blank=True)
