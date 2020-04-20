# Generated by Django 3.0.2 on 2020-01-14 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto_Onix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.CharField(max_length=70)),
                ('volume', models.DecimalField(decimal_places=3, max_digits=7)),
                ('unidade', models.CharField(choices=[('Kg', 'kilos'), ('g', 'gramas'), ('L', 'litros'), ('ml', 'mililitros'), ('cx', 'caixa')], max_length=2)),
                ('descricao', models.CharField(max_length=80)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cadastro Onix',
                'verbose_name_plural': '1.0 - Cadastro Onix',
                'ordering': ['volume', 'familia'],
            },
        ),
        migrations.CreateModel(
            name='Produto_Syngenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField()),
                ('familia', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=50)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('produto_onix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synprodutos.Produto_Onix')),
            ],
            options={
                'verbose_name': 'Cadastro Syngenta',
                'verbose_name_plural': '2.0 - Cadastro Syngenta',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='DePara_OnixDistribuidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_onix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synprodutos.Produto_Onix')),
            ],
        ),
    ]
