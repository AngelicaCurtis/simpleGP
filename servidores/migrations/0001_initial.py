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
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Área')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=1, verbose_name='Nível')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siape', models.CharField(max_length=7, unique=True, verbose_name='SIAPE')),
                ('nome', models.CharField(help_text='Obrigatório', max_length=50)),
                ('sobrenome', models.CharField(max_length=200)),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('1', 'Feminino'), ('2', 'Masculino')], max_length=1)),
                ('tipo_sanguineo', models.CharField(choices=[('1', 'A+'), ('2', 'B+'), ('3', 'AB+'), ('4', 'O+'), ('5', 'A-'), ('6', 'B-'), ('7', 'AB-'), ('8', 'O-')], max_length=1, verbose_name='Tipo Sanguíneo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('naturalidade', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_servidores', verbose_name='Foto Perfil')),
                ('data_exercicio', models.DateField(verbose_name='Data de Exercício')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='servidores.Area')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campi.Campus')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='servidores.Cargo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servidores.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Servidores',
                'permissions': (('cadastrar_servidor', 'Usuário pode cadastrar novo servidor'), ('visualizar_servidor', 'Usuário pode visualizar cadastro de servidor'), ('atualizar_servidor', 'Usuário pode atualizar informações'), ('deletar_servidor', 'Usuário pode deletar o cadastro do servidor')),
            },
        ),
        migrations.AddField(
            model_name='cargo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servidores.Categoria'),
        ),
        migrations.AddField(
            model_name='area',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servidores.Categoria'),
        ),
        migrations.AlterUniqueTogether(
            name='servidor',
            unique_together={('siape', 'nome', 'cargo'), ('siape', 'nome', 'area')},
        ),
    ]
