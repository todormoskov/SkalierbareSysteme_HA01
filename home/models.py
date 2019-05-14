from django.db import models

# Create your models here.
class Aufgaben(models.Model):
    aufgabe = models.TextField(max_length=160)
    deadline = models.DateField()
    status = models.IntegerField()
