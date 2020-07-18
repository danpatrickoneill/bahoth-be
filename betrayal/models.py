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
  hobbies = models.CharField(max_length=100)
  speed = models.IntegerField()
  might = models.IntegerField()
  sanity = models.IntegerField()
  knowledge = models.IntegerField()

class Room(models.Model):
    ITEM = 'I'
    MULTIPLE_ITEMS = 'II'
    EVENT = 'E'
    OMEN = 'O'
    CARD_CHOICES = [
      (ITEM, 'Item'),
      (MULTIPLE_ITEMS, 'Multiple Items'),
      (EVENT, 'Event'),
      (OMEN, 'Omen'),
    ]
  name = models.CharField(max_length=100)
  card = models.IntegerField(choices=CARD_CHOICES)
  effect = models.CharField(max_length=100)

class Item(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  # Could this be a "holder/location" field that could be either a character or room? Could be useful
  character = models.ForeignKey(
    'Character',
    on_delete=models.CASCADE
  )

