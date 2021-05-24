# Generated by Django 3.2.3 on 2021-05-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomCommerciale', models.CharField(max_length=200, null=True)),
                ('Nature', models.CharField(max_length=200, null=True)),
                ('Libellé', models.CharField(max_length=200, null=True)),
                ('PubliqueCible', models.CharField(max_length=200, null=True)),
                ('CategirieProfessionnelle', models.CharField(max_length=200, null=True)),
                ('Duré de conservation', models.CharField(max_length=200, null=True)),
                ('Forme galinique', models.CharField(max_length=200, null=True)),
                ('DemandeAMM', models.CharField(max_length=200, null=True)),
                ('VoiAdministration', models.CharField(max_length=200, null=True)),
                ('Fabriquant', models.CharField(max_length=200, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]