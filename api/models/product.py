from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
