# Generated by Django 3.2.3 on 2021-05-21 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Composition', '0002_auto_20210520_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
    ]