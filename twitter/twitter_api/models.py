from django.db import models

# Create your models here.

class Tweet(models.Model):
    name=models.CharField(max_length=20)
    text=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True)