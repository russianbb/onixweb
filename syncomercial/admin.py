from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin 
from nested_admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

from .models import Distribuidor, Filial, Responsavel, Responsavel_Distribuidor, RTV, RTV_Distribuidor


class RTVAdmin(SimpleHistoryAdmin):
    #Classe que controla a exibição do model "Responsavel_Distribuidor" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['nome', 'code_spoca', 'email', 'ddd1', 'telefone1', 'ddd2', 'telefone2']
    list_display_links = ['nome', 'code_spoca', 'email', 'ddd1', 'telefone1', 'ddd2', 'telefone2']
    search_fields = ['nome', 'code_spoca', 'email', 'ddd1', 'telefone1', 'ddd2', 'telefone2']

class RTV_DistribuidorNestedInLine(NestedStackedInline):
    #Classe que controla exclusivamente a exibição do Responsável_Distribuidor na página do distribuidor
    model = RTV_Distribuidor
    extra = 0


class RTV_DistribuidorAdmin(SimpleHistoryAdmin):
    #Classe que controla a exibição do model "Responsavel_Distribuidor" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['distribuidor', 'RTV']
    #list_display_links = ['distribuidor', 'responsavel']
    #search_fields = ['responsavel_id__nome', 'responsavel_id__tipo_atuacao', 'responsavel_id__telefone1', 'responsavel_id__telefone2']



class ResponsavelAdmin(SimpleHistoryAdmin):
    list_display = ['nome', 'cargo', 'tipo_atuacao', 'email', 'ddd1', 'telefone1', 'ddd2', 'telefone2']
    list_display_links = ['nome', 'cargo', 'tipo_atuacao', 'email']
    search_fields = ['nome', 'cargo', 'tipo_atuacao', 'email', 'ddd1', 'telefone1', 'ddd2', 'telefone2', 'anotacao']




class Responsavel_DistribuidorNestedInLine(NestedStackedInline):
    #Classe que controla exclusivamente a exibição do Responsável_Distribuidor na página do distribuidor
    model = Responsavel_Distribuidor
    extra = 0


class Responsavel_DistribuidorAdmin(SimpleHistoryAdmin):
    #Classe que controla a exibição do model "Responsavel_Distribuidor" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['distribuidor', 'responsavel', 'atuacao', 'telefone1', 'telefone2', 'atualizado_em']
    list_display_links = ['distribuidor', 'responsavel']
    search_fields = ['responsavel_id__nome', 'responsavel_id__tipo_atuacao', 'responsavel_id__telefone1', 'responsavel_id__telefone2']




class Responsavel_FilialNestedInLine(NestedStackedInline):
    #Classe que controla exclusivamente a exibição do Responsável_Filial na página da filial
    model = Responsavel_Filial
    extra = 0


class Responsavel_FilialAdmin(SimpleHistoryAdmin):
    #Classe que controla a exibição do model "Responsavel_Filial" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['distribuidor', 'responsavel', 'atuacao', 'telefone1', 'telefone2', 'atualizado_em']
    list_display_links = ['distribuidor', 'responsavel']
    search_fields = ['filial_id__distribuidor_id__razao_social', 'responsavel_id__nome', 'responsavel_id__tipo_atuacao', 'responsavel_id__telefone1', 'responsavel_id__telefone2']


class FilialNestedInLine(NestedStackedInline):
    #Classe que controle exclusivamente a exibição da filial na página do distribuidor
    model = Filial
    extra = 0
    
    inlines = [Responsavel_FilialNestedInLine]

class FilialAdmin(SimpleHistoryAdmin, NestedModelAdmin):
    #Classe que controla a exibição do model "Filial" em sua página EXCLUSIVA do admin
    #Default Part
    list_display = ['distribuidor', 'cidade', 'estado', 'slug', 'codigo_local', 'cnpj']
    list_display_links = ['distribuidor', 'cidade', 'estado', 'slug', 'codigo_local', 'cnpj']
    search_fields = ['filial_id__distribuidor_id__razao_social', 'responsavel_id__nome', 'responsavel_id__tipo_atuacao', 'responsavel_id__telefone1', 'responsavel_id__telefone2']


    #Nested Part
    model = Filial
    inlines = [Responsavel_FilialNestedInLine]



class DistribuidorAdmin(SimpleHistoryAdmin, NestedModelAdmin):
    #Classe que controla a exibição do model "Distribuidor" em sua página EXCLUSIVA do admin
    #Para exibir filial "nested" a esse model, herda também o NestedModelAdmin.
    #Default Part
    list_display = ['razao_social', 'code_sap', 'nome_fantasia', 'atualizado_em'] #@todo adicionar RTV
    list_display_links = ['razao_social', 'code_sap', 'nome_fantasia']
    search_fields = ['razao_social', 'code_sap', 'nome_fantasia']


    #SimpleHistory - não necessária até o momento
    
    #Nested Part
    model = Distribuidor
    inlines = [RTV_DistribuidorNestedInLine ,Responsavel_DistribuidorNestedInLine, FilialNestedInLine]


# Register your models here.
admin.site.register(Distribuidor, DistribuidorAdmin)
admin.site.register(Filial, FilialAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(Responsavel_Filial, Responsavel_FilialAdmin)
admin.site.register(Responsavel_Distribuidor, Responsavel_DistribuidorAdmin)
admin.site.register(RTV, RTVAdmin)
admin.site.register(RTV_Distribuidor, RTV_DistribuidorAdmin)
