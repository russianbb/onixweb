from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here

class Distribuidor(models.Model):
    code_sap = models.CharField(max_length = 8)
    razao_social = models.CharField(max_length = 100)
    nome_fantasia = models.CharField(max_length = 50)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    historico = HistoricalRecords()
 
    def __str__(self):
        return self.razao_social
    
    class Meta:
        ordering = ['razao_social']
        verbose_name = 'Distribuidor'
        verbose_name_plural = '2.0 - Cadastro de Distribuidores'


class Filial(models.Model):
    distribuidor_id = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    codigo_local = models.CharField(max_length = 100, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    cnpj = models.CharField(max_length = 14)
    endereco = models.CharField(max_length = 200)
    cidade = models.CharField(max_length = 50)
    estado = models.CharField(max_length = 2)
    cod_ibge = models.CharField(max_length = 9, null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    controla_estoque = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    historico = HistoricalRecords()
   
    def __str__(self):
        return f"{self.distribuidor_id.razao_social} - {self.slug}"

    def distribuidor(self):
        return self.distribuidor_id.razao_social

    class Meta():
        ordering = ['distribuidor_id', 'cidade', 'slug']
        verbose_name = 'Filial'
        verbose_name_plural = '2.1 - Cadastro de Filiais'
    

class Responsavel(models.Model):
    nome = models.CharField(max_length = 40)
    cargo = models.CharField(max_length = 20, null=True, blank=True)
    tipo_atuacao = models.CharField(max_length = 40)
        ### Pode ser um "option field" no futuro... @todo
    email = models.EmailField(null=True, blank=True)
    ddd1 = models.CharField(max_length = 2, null=True, blank=True)
    telefone1 = models.CharField(max_length = 9, null=True, blank=True)
    ramal1 = models.CharField(max_length = 4, null=True, blank=True)
    ddd2 = models.CharField(max_length = 2, null=True, blank=True)
    telefone2 = models.CharField(max_length = 9, null=True, blank=True)
    ramal2 = models.CharField(max_length = 4, null=True, blank=True)
    anotacao = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    historico = HistoricalRecords()

    def __str__(self):
        if self.ddd1 and self.telefone1:
            return f"{self.nome} - ({self.ddd1}) {self.telefone1[-9:-4]}-{self.telefone1[-4:]}"
        else:
            return self.nome

    class Meta():
        ordering = ['nome']
        verbose_name = 'Responsavel'
        verbose_name_plural = '3.0 - Cadastro de Responsáveis'


class Responsavel_Distribuidor(models.Model):
    distribuidor_id = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    responsavel_id = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    historico = HistoricalRecords()

    def __str__(self):
        return self.distribuidor_id.razao_social

    def distribuidor(self):
        return self.distribuidor_id.razao_social

    def responsavel(self):
        return self.responsavel_id.nome

    def atuacao(self):
        return self.responsavel_id.tipo_atuacao

    def telefone1(self):
        if self.responsavel_id.ddd1 and self.responsavel_id.telefone1:
            return f'({self.responsavel_id.ddd1}) {self.responsavel_id.telefone1[-9:-4]}-{self.responsavel_id.telefone1[-4:]}'

    def telefone2(self):
        if self.responsavel_id.ddd2 and self.responsavel_id.telefone2:
            return f'({self.responsavel_id.ddd2}) {self.responsavel_id.telefone2[-9:-4]}-{self.responsavel_id.telefone2[-4:]}'

    class Meta:
        ordering = ['distribuidor_id', 'responsavel_id']
        unique_together = ('distribuidor_id', 'responsavel_id')
        verbose_name = 'Responsável pelo Distribuidor'
        verbose_name_plural = '9.2 - Responsável pelo Distribuidor'

# Esse modelo esta temporariamente desativado.
# Provavelmente irei incluir esses dados no cadastro da filial @todo
# class Responsavel_Filial(models.Model):
#     filial_id = models.ForeignKey(Filial, on_delete=models.CASCADE)
#     responsavel_id = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
#     criado_em = models.DateTimeField(auto_now_add=True)
#     atualizado_em = models.DateTimeField(auto_now=True)
#     status = models.BooleanField(default=True)
#     historico = HistoricalRecords()

#     def __str__(self):
#         return f"{self.filial_id.distribuidor_id.razao_social} - {self.responsavel_id.nome}"

#     def distribuidor(self):
#         return self.filial_id.distribuidor_id.razao_social

#     def local(self):
#         return f"{self.filial_id.cidade} / {self.filial_id.estado}"
    
#     def unidade(self):
#         return f"{self.filial_id.slug} - {self.filial_id.codigo_local}"

#     def responsavel(self):
#         return self.responsavel_id.nome

#     def atuacao(self):
#         return self.responsavel_id.tipo_atuacao

#     def telefone1(self):
#         return f'({self.responsavel_id.ddd1}) {self.responsavel_id.telefone1[-9:-4]}-{self.responsavel_id.telefone1[-4:]}'

#     def telefone2(self):
#         if self.responsavel_id.ddd2 and self.responsavel_id.telefone2:
#             return f'({self.responsavel_id.ddd2}) {self.responsavel_id.telefone2[-9:-4]}-{self.responsavel_id.telefone2[-4:]}'

#     class Meta:
#         ordering = ['filial_id', 'responsavel_id']
#         unique_together = ('filial_id', 'responsavel_id')
#         verbose_name = 'Responsável pela Filial'
#         verbose_name_plural = '9.3 - Responsável pela Filial'


class RTV(models.Model):
    nome = models.CharField(max_length = 40)
    code_spoca = models.CharField(max_length = 8, null=True, blank=True)
    email = models.EmailField()
    ddd1 = models.CharField(max_length=2, null=True, blank=True)
    telefone1 = models.CharField(max_length=9, null=True, blank=True)
    ramal1 = models.CharField(max_length=4, null=True, blank=True)
    ddd2 = models.CharField(max_length=2, null=True, blank=True)
    telefone2 = models.CharField(max_length=9, null=True, blank=True)
    ramal2 = models.CharField(max_length=4, null=True, blank=True)
    anotacao = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    historico = HistoricalRecords()

    def __str__(self):
        if self.ddd1 and self.telefone1:
            return f"{self.nome} - ({self.ddd1}) {self.telefone1[-9:-4]}-{self.telefone1[-4:]}"
        else:
            return self.nome

    def RTV(self):
        return {self.nome}
    
    def contato1(self):
        if self.ddd1 and self.telefone1:
            return f'({self.ddd1}) {self.telefone1[-9:-4]}-{self.telefone1[-4:]}'

    def contato2(self):
        if self.ddd2 and self.telefone2:
            return f'({self.ddd2}) {self.telefone2[-9:-4]}-{self.telefone2[-4:]}'

    class Meta():
        ordering = ['nome']
        verbose_name = 'RTV'
        verbose_name_plural = '1.0 - Cadastro de RTVs'

class RTV_Distribuidor(models.Model):
    distribuidor_id = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    RTV_id = models.ForeignKey(RTV, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    historico = HistoricalRecords()

    def __str__(self):
        return self.distribuidor_id.razao_social

    def distribuidor(self):
        return self.distribuidor_id.razao_social

    def RTV(self):
        return self.RTV_id.nome

    def contato1(self):
        if self.RTV_id.ddd1 and self.RTV_id.telefone1:
            return f'({self.RTV_id.ddd1}) {self.RTV_id.telefone1[-9:-4]}-{self.RTV_id.telefone1[-4:]}'

    def telefone2(self):
        if self.RTV_id.ddd2 and self.RTV_id.telefone2:
            return f'({self.RTV_id.ddd2}) {self.RTV_id.telefone2[-9:-4]}-{self.RTV_id.telefone2[-4:]}'

    class Meta:
        ordering = ['distribuidor_id', 'RTV_id__nome']
        unique_together = ('distribuidor_id', 'RTV_id')
        verbose_name = 'RTV do Distribuidor'
        verbose_name_plural = '9.1 - RTV do Distribuidor'