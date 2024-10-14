from django.db import models

# Create your models here.
class abid_blog(models.Model):
    title = models.CharField(max_length=200)