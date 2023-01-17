from django.db import models

# Create your models here.
class ad(models.Model):
    id = models.PositiveSmallIntegerField(primary_key = True, null = False, unique = True)
    name = models.TextField(max_length = 255)
    author = models.TextField(max_length = 255)
    price = models.DecimalField(max_digits = 12, decimal_places=2)
    description = models.TextField(max_length = 2048)
    address = models.CharField(max_length = 200)
    is_published = models.BooleanField(null = False)

class category(models.Model):
    id = models.PositiveSmallIntegerField(primary_key = True, null = False, unique = True)
    category = models.TextField(max_length = 255)