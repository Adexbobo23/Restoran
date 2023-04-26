from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2)
    desc = models.TextField()
