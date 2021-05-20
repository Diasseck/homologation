# Generated by Django 3.2.3 on 2021-05-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Composition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('en instance', 'en instance'), ('non livre', 'non livre'), ('livre', 'livre')], max_length=200, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Composition',
        ),
    ]