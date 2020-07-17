from django.db import models
from uuid import uuid4

# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  age = models.IntegerField()
  height = models.IntegerField()
  weight = models.IntegerField()
  birthday = models.DateField()
  description = models.TextField(blank=True)
  speed = models.IntegerField()
  might = models.IntegerField()
  sanity = models.IntegerField()
  knowledge = models.IntegerField()


