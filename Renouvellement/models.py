from django.db import models

# Create your models here.

class Produit(models.Model):
    ('idRenouvellement', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    ('laboratoire', models.CharField(max_length=200, null=True)),
    ('quitance', models.FloatField(null=True)),
    ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),

