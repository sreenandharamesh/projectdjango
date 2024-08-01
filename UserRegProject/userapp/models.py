from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 20)
    title = models.CharField(max_length = 40)
    content = models.CharField(max_length=200)
    date = models.DateField()