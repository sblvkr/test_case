from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_length=6, max_digits=2)
