
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin 
from nested_admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

from .models import Distribuidor, Filial, Responsavel, Responsavel_Distribuidor, RTV, RTV_Distribuidor

class RTV_Distribuidor_Aninhado(NestedStackedInline):
    #Classe que controla exclusivamente a exibição do "Responsável_Distribuidor" na página do distribuidor
    model = RTV_Distribuidor
    extra = 0


class Filial_Aninhado(NestedStackedInline):
    #Classe que controle exclusivamente a exibição da filial na página do distribuidor
    model = Filial
    extra = 0

##########################################################################################################################################

class DistribuidorAdmin(SimpleHistoryAdmin, NestedModelAdmin):
    #Classe que controla a exibição do model "Distribuidor" em sua página EXCLUSIVA do admin
    #Para exibir filial "nested" a esse model, herda também o NestedModelAdmin.
    #Default Part
    list_display = ['razao_social', 'code_sap', 'nome_fantasia', 'atualizado_em']
    list_display_links = ['razao_social', 'code_sap', 'nome_fantasia']
    search_fields = ['razao_social', 'code_sap', 'nome_fantasia']


    #SimpleHistory - não necessária até o momento
    
    #Nested Part
    model = Distribuidor
    inlines = [RTV_Distribuidor_Aninhado ,Filial_Aninhado]


class FilialAdmin(SimpleHistoryAdmin, NestedModelAdmin):
    #Classe que controla a exibição do model "Filial" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['distribuidor', 'cidade', 'estado', 'codigo', 'nome', 'cnpj']
    list_display_links = ['distribuidor', 'cidade', 'estado', 'codigo',  'nome','cnpj']


class RTVAdmin(SimpleHistoryAdmin):
    #Classe que controla a exibição do model "RTV" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['nome', 'code_spoca', 'email', 'contato1', 'contato2']
    list_display_links = ['nome', 'code_spoca', 'email', 'contato1', 'contato2']
    search_fields = ['nome', 'code_spoca', 'email', 'ddd1', 'telefone1', 'ddd2', 'telefone2']


class RTV_DistribuidorAdmin(SimpleHistoryAdmin):
    #Classe que controla a exibição do model "RTV do Distribuidor" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['distribuidor', 'RTV']
    list_display_links = ['distribuidor', 'RTV']


class ResponsavelAdmin(SimpleHistoryAdmin):
    #Classe que controla a exibição do model "Responsavel" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['nome', 'cargo', 'atuacao', 'email', 'contato1', 'contato2']
    list_display_links = ['nome', 'cargo', 'atuacao', 'email', 'contato1', 'contato2']
    search_fields = ['nome', 'cargo', 'atuacao', 'email', 'ddd1', 'telefone1', 'ddd2', 'telefone2', 'anotacao']


# Register your models here.
admin.site.register(Distribuidor, DistribuidorAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(Filial, FilialAdmin)
admin.site.register(RTV, RTVAdmin)
