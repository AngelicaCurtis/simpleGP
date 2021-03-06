# Generated by Django 2.1 on 2018-11-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.CharField(choices=[('1', 'Primeira'), ('2', 'Segunda'), ('3', 'Terceira'), ('4', 'Quarta')], max_length=1)),
                ('data', models.DateField(blank=True, null=True)),
                ('nota_aval_servidor', models.IntegerField(blank=True, null=True)),
                ('nota_aval_chefia', models.IntegerField(blank=True, null=True)),
                ('media_aval', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstagioProbatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Estágios Probatórios',
            },
        ),
    ]
