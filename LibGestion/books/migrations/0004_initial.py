# Generated by Django 4.0.4 on 2022-05-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Identifiant', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=30)),
                ('Prenom', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('MotDePasse', models.CharField(max_length=30)),
            ],
        ),
    ]