from django.db import models

# Create your models here.


class Recipt(models.Model):
    title = models.CharField(max_length=255)
    ing = models.TextField()
    recipt = models.TextField()
    Author = models.CharField(max_length=255)