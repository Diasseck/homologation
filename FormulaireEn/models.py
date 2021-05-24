from django.db import models


class FormulaireEn(models.Model):
    ('NomCommerciale', models.CharField(max_length=200, null=True)),
    ('Nature', models.CharField(max_length=200, null=True)),
    #('Libellé', models.CharField(max_length=200, null=True)),
    #('PubliqueCible', models.CharField(max_length=200, null=True)),
    #('CategirieProfessionnelle', models.CharField(max_length=200, null=True)),
    #('Duré de conservation', models.CharField(max_length=200, null=True)),
    #('Forme galinique', models.CharField(max_length=200, null=True)),
    #('DemandeAMM', models.CharField(max_length=200, null=True)),
    #('VoiAdministration', models.CharField(max_length=200, null=True)),
    #('Fabriquant', models.CharField(max_length=200, null=True)),
    #('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
