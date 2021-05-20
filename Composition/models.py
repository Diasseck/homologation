from django.db import models
from django.db.models import CharField

from Medicament.models import Medicament
from Renouvellement.models import Produit

# Create your models here.

class Commande(models.Model):
    STATUS=(('en instance','en instance'),('non livre','non livre'),('livre','livre'))
    #Medicament=
    #Renouvellement=
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)

