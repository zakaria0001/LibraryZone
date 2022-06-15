from django.db import models

# Create your models here.
class User (models.Model):
    Id = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Username = models.CharField(max_length=30,null=False)
    Email = models.CharField(max_length=30)
    MotDePasse = models.CharField(max_length=30)


class book (models.Model):
    IdB = models.IntegerField(primary_key=True)
    Nom= models.CharField(max_length=128)
    Categorie = models.CharField(max_length=30)
    Auteur = models.CharField(max_length=30)
    Classement = models.CharField(max_length=30)
 
class book_fav (models.Model):
      NomLivre = models.CharField(max_length=30)
      Username = models.CharField(max_length=30)

class FeedBack(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    NumeroDeTelephone = models.CharField(max_length=14)
    Message = models.CharField(max_length=400)