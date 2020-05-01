# Generated by Django 3.0.2 on 2020-05-01 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_sap', models.CharField(max_length=8, unique=True)),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=50)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Distribuidor',
                'verbose_name_plural': '1.0 - Cadastro de Distribuidores',
                'ordering': ['razao_social'],
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cargo', models.CharField(blank=True, max_length=30, null=True)),
                ('atuacao', models.CharField(choices=[('Crop', 'Crop'), ('Seeds', 'Seeds'), ('Ambos', 'Ambos')], max_length=5)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ddd1', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone1', models.CharField(blank=True, max_length=9, null=True)),
                ('ramal1', models.CharField(blank=True, max_length=4, null=True)),
                ('ddd2', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=9, null=True)),
                ('ramal2', models.CharField(blank=True, max_length=4, null=True)),
                ('anotacao', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': '3.0 - Cadastro de Responsáveis',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='RTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('code_spoca', models.CharField(blank=True, max_length=8, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ddd1', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone1', models.CharField(blank=True, max_length=9, null=True)),
                ('ramal1', models.CharField(blank=True, max_length=4, null=True)),
                ('ddd2', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=9, null=True)),
                ('ramal2', models.CharField(blank=True, max_length=4, null=True)),
                ('anotacao', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'RTV',
                'verbose_name_plural': '2.0 - Cadastro de RTVs',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalRTV_Distribuidor',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('atualizado_em', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('RTV', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='syncomercial.RTV')),
                ('distribuidor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='syncomercial.Distribuidor')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical RTV do Distribuidor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRTV',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('code_spoca', models.CharField(blank=True, max_length=8, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ddd1', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone1', models.CharField(blank=True, max_length=9, null=True)),
                ('ramal1', models.CharField(blank=True, max_length=4, null=True)),
                ('ddd2', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=9, null=True)),
                ('ramal2', models.CharField(blank=True, max_length=4, null=True)),
                ('anotacao', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('atualizado_em', models.DateTimeField(blank=True, editable=False)),
                ('status', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical RTV',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalResponsavel_Distribuidor',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('atualizado_em', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('distribuidor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='syncomercial.Distribuidor')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('responsavel', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='syncomercial.Responsavel')),
            ],
            options={
                'verbose_name': 'historical Responsável pelo Distribuidor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalResponsavel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cargo', models.CharField(blank=True, max_length=30, null=True)),
                ('atuacao', models.CharField(choices=[('Crop', 'Crop'), ('Seeds', 'Seeds'), ('Ambos', 'Ambos')], max_length=5)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ddd1', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone1', models.CharField(blank=True, max_length=9, null=True)),
                ('ramal1', models.CharField(blank=True, max_length=4, null=True)),
                ('ddd2', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=9, null=True)),
                ('ramal2', models.CharField(blank=True, max_length=4, null=True)),
                ('anotacao', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('atualizado_em', models.DateTimeField(blank=True, editable=False)),
                ('status', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Responsável',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFilial',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('cnpj', models.CharField(max_length=14)),
                ('responsavel', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ddd', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True)),
                ('endereco', models.CharField(max_length=250)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('codibge', models.CharField(blank=True, max_length=9, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('controla_estoque', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('atualizado_em', models.DateTimeField(blank=True, editable=False)),
                ('status', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('distribuidor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='syncomercial.Distribuidor')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Filial',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDistribuidor',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('code_sap', models.CharField(db_index=True, max_length=8)),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=50)),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('atualizado_em', models.DateTimeField(blank=True, editable=False)),
                ('status', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Distribuidor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='RTV_Distribuidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('RTV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syncomercial.RTV')),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syncomercial.Distribuidor')),
            ],
            options={
                'verbose_name': 'RTV do Distribuidor',
                'verbose_name_plural': '9.1 - RTV do Distribuidor',
                'ordering': ['distribuidor__razao_social', 'RTV__nome'],
                'unique_together': {('distribuidor', 'RTV')},
            },
        ),
        migrations.CreateModel(
            name='Responsavel_Distribuidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syncomercial.Distribuidor')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syncomercial.Responsavel')),
            ],
            options={
                'verbose_name': 'Responsável pelo Distribuidor',
                'verbose_name_plural': '9.2 - Responsável pelo Distribuidor',
                'ordering': ['distribuidor__razao_social', 'responsavel__nome'],
                'unique_together': {('distribuidor', 'responsavel')},
            },
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('cnpj', models.CharField(max_length=14)),
                ('responsavel', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ddd', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True)),
                ('endereco', models.CharField(max_length=250)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('codibge', models.CharField(blank=True, max_length=9, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('controla_estoque', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syncomercial.Distribuidor')),
            ],
            options={
                'verbose_name': 'Filial',
                'verbose_name_plural': '1.1 - Cadastro de Filiais',
                'ordering': ['distribuidor__razao_social', 'cidade', 'nome'],
                'unique_together': {('cnpj', 'codigo', 'nome', 'distribuidor_id')},
            },
        ),
    ]
