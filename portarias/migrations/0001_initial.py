# Generated by Django 2.1 on 2018-11-25 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=4)),
                ('ano', models.SmallIntegerField()),
                ('descricao', models.CharField(max_length=200)),
                ('portaria', models.FileField(blank=True, null=True, upload_to='portarias')),
                ('origem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campi.Campus')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='portaria',
            unique_together={('numero', 'ano', 'origem')},
        ),
    ]
