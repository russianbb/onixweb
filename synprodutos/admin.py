from django.contrib import admin
from nested_admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

# Register your models here.
from .models import Produto_Onix, Produto_Syngenta, Produto_Distribuidor

class Produto_SyngentaNested(NestedTabularInline):
    model = Produto_Syngenta
    extra = 0


############################################################################################################


class Produto_OnixAdmin(NestedModelAdmin):
    list_display = ('id', 'descricao', 'atualizado_em')
    list_display_links = ('id', 'descricao', 'atualizado_em')
    search_fields = ('id', 'descricao', 'produto', 'volume', 'unidade', 'atualizado_em')

    model = Produto_Onix
    inlines = [Produto_SyngentaNested]


class Produto_SyngentaAdmin(admin.ModelAdmin):
    list_display = ('agicode', 'descricao', 'familia', 'produto_onix_id', 'onix_descricao', 'atualizado_em')
    list_display_links = ('agicode', 'descricao', 'familia', 'atualizado_em')
    search_fields = ('agicode', 'descricao', 'familia', 'atualizado_em')


class Produto_DistribuidorAdmin(admin.ModelAdmin):
    list_display = ('distribuidor', 'codigo', 'descricao', 'onix_id', 'onix_descricao', 'atualizado_em')
    list_display_links = ('codigo', 'descricao')
    search_fields = ('codigo', 'descricao')



admin.site.register(Produto_Onix, Produto_OnixAdmin)
admin.site.register(Produto_Syngenta, Produto_SyngentaAdmin)
admin.site.register(Produto_Distribuidor, Produto_DistribuidorAdmin)