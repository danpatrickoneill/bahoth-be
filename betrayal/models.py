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
  hero = models.BooleanField(default=False)
  traitor = models.BooleanField(default=False)

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
  omen = models.BooleanField(default=False)

# Would it make sense to have a separate monster model? Could have a more basic "living thing" model that other can inherit from. 
# I don't think heros and traitors would need a distinct model, but then the standard character model might need some rarely used fields
# Game manual calls PCs "explorers"; both they and monsters could inherit from character