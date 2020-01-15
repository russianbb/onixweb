from django.db import models
from simple_history.models import HistoricalRecords
from syncomercial.models import Distribuidor

# Create your models here.



class Produto_Onix(models.Model):
    unidade_choices = (
        ('Kg', 'kilos'),
        ('g', 'gramas'),
        ('L', 'litros'),
        ('ml', 'mililitros'),
        ('cx', 'caixa')
    )
    familia = models.CharField(max_length=70)
    volume = models.DecimalField(max_digits=7, decimal_places=3)
    unidade = models.CharField(max_length=2, choices=unidade_choices)
    descricao = models.CharField(max_length=80)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['volume', 'familia']
        verbose_name = 'Cadastro Onix'
        verbose_name_plural = '1.0 - Cadastro Onix'
    
    def __str__(self):
        return f'{self.id} - {self.descricao}'


class Produto_Syngenta(models.Model):
    produto_onix = models.ForeignKey(Produto_Onix, on_delete=models.CASCADE)
    codigo = models.PositiveIntegerField()
    familia = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['descricao']
        verbose_name = 'Cadastro Syngenta'
        verbose_name_plural = '2.0 - Cadastro Syngenta'

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'

    def onix_id(self):
        return f'{self.produto_onix.id}'

    def onix_descricao(self):
        return f'{self.produto_onix.descricao}'


class Produto_Distribuidor(models.Model):
    produto_onix = models.ForeignKey(Produto_Onix, on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=80)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['distribuidor__razao_social', 'descricao']
        verbose_name = 'Cadastro Distribuidor'
        verbose_name_plural = '3.0 - Cadastro Distribuidor'

    def __str__(self):
        return f'{self.distribuidor.razao_social} - {self.produto_onix.descricao}'

    def onix_id(self):
        return f'{self.produto_onix.id}'

    def onix_descricao(self):
        return f'{self.produto_onix.descricao}'