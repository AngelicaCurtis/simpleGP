# Generated by Django 2.1 on 2018-09-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servidores', '0004_delete_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
