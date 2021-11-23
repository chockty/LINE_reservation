from django.db import models
from django.db.models.expressions import Value
from django.db.models.fields import IntegerField

# Create your models here.

class User(models.Model):
  user_id = models.IntegerField()
  name = models.CharField(max_length=20)
  name_kana = models.CharField(max_length=20)
  zipcode = models.IntegerField(max_length=10)
  address = models.CharField(max_length=100)
  tel = models.IntegerField(max_length=15)
  active = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.name

class Reservation(models.Model):
  reservation_id = models.IntegerField()
  user_id = models.IntegerField()
  choice_id = models.IntegerField()
  value = models.CharField(max_length=100)

  def __str__(self):
      return self.reservation_id

class ReservationsChoice(models.Model):
  choice_id = models.IntegerField()
  name = models.CharField(max_length=100)
  type = models.IntegerField()

  def __str__(self):
      return self.name