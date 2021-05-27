from django.db import models


class AMM(models.Model):
    ('Name', models.CharField(max_length=200, null=True)),
    ('Fabriquant', models.CharField(max_length=200, null=True)),
    ('Titulaire', models.CharField(max_length=200, null=True)),
    ('Forme', models.CharField(max_length=200, null=True)),
    ('Voie', models.CharField(max_length=200, null=True))
