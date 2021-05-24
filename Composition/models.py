from django.db import models
from django.db.models import CharField

from Medicament.models import Medicament
from Renouvellement.models import Renouvellement

# Create your models here.

class Composition(models.Model):
    #Medicament=
    #Renouvellement=
    status=models.CharField(max_length=200,null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)

