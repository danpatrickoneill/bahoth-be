from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Does it make sense to have a Game model that could be saved as an instance with Chars linked to it? Good to research
class Character(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  speed = models.IntegerField()
  might = models.IntegerField()
  sanity = models.IntegerField()
  knowledge = models.IntegerField()

  class Meta:
    abstract = True

class PlayerCharacter(Character):
  user = user.OneToOneField(User, on_delete=models.CASCADE)
  age = models.IntegerField()
  height = models.IntegerField()
  weight = models.IntegerField()
  birthday = models.DateField()
  hobbies = models.CharField(max_length=100)
  hero = models.BooleanField(default=False)
  traitor = models.BooleanField(default=False)

class Monster(Character):

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