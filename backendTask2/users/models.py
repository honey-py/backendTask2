from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30)
    username = models.CharField(max_length =30)
    email = models.EmailField()
    password = models.CharField(max_length =30)