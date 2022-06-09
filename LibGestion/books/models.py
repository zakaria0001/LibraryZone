from django.db import models
from django.forms import CharField

class Utilisateur (models.Model):
    Identifiant = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    MotDePasse = models.CharField(max_length=30)
 