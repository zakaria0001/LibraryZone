# Generated by Django 4.0.4 on 2022-05-24 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_rename_user_utilisateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='Identifiant',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]