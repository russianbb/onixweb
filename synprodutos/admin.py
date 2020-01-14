from django.contrib import admin
from nested_admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

# Register your models here.
from .models import Produto_Onix, Produto_Syngenta

class Produto_SyngentaNested(NestedTabularInline):
    model = Produto_Syngenta
    extra = 0


############################################################################################################


class Produto_SyngentaAdmin(admin.ModelAdmin):
    list_display = ('onix_id', 'codigo', 'descricao', 'familia', 'atualizado_em')
    list_display_links = ('codigo', 'descricao', 'familia', 'atualizado_em')
    search_fields = ('codigo', 'descricao', 'familia', 'atualizado_em')


class Produto_OnixAdmin(NestedModelAdmin):
    list_display = ('descricao', 'familia', 'volume', 'unidade', 'atualizado_em')
    list_display_links = ('descricao', 'familia', 'volume', 'unidade', 'atualizado_em')
    search_fields = ('descricao', 'produto', 'volume', 'unidade', 'atualizado_em')

    model = Produto_Onix
    inlines = [Produto_SyngentaNested]

admin.site.register(Produto_Onix, Produto_OnixAdmin)
admin.site.register(Produto_Syngenta, Produto_SyngentaAdmin)