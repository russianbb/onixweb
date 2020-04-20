from django.urls import path, include

from . import views

app_name = 'syncomercial'

urlpatterns = [
    path('', views.index, name='index'),
    path('distribuidores/', views.distribuidores, name='distribuidores'),
    path('distribuidores/<int:distribuidor_id>/', views.distribuidor_detalhe, name='distribuidor_detalhe'),
    path('filial/<int:filial_id>/', views.filial_detalhe, name='filial_detalhe'),
    path('filial/editar/<int:filial_id>/', views.filial_editar, name='filial_editar'),
    path('filial/adicionar/<int:distribuidor_id>/', views.filial_adicionar, name='filial_adicionar'),
    
    
    path('rtvs/', views.rtvs, name='rtvs'),
    path('rtvs/<int:rtv_id>', views.rtv_detalhe, name='rtv_detalhe'),
    path('rtvs/editar/<int:rtv_id>', views.rtv_editar, name='rtv_editar'),
    path('rtvs/adicionar', views.rtv_adicionar, name='rtv_adicionar'),
    
    path('rtvs/atribuir/<distribuidor_id>/', views.rtv_atribuir, name='rtv_atribuir'),
    path('rtvs/desatribuir/<rtv_id>&<distribuidor_id>/', views.rtv_desatribuir, name='rtv_desatribuir'),
    
    path('responsaveis/', views.responsaveis, name='responsaveis'),
    path('responsaveis/<int:responsavel_id>', views.responsavel_detalhe, name='responsavel_detalhe'),
    path('responsaveis/editar/<int:responsavel_id>', views.responsavel_editar, name='responsavel_editar'),
    path('responsaveis/adicionar', views.responsavel_adicionar, name='responsavel_adicionar'),
    
    path('responsaveis/atribuir/<distribuidor_id>/', views.responsavel_atribuir, name='responsavel_atribuir'),
    path('responsaveis/desatribuir/<responsavel_id>&<distribuidor_id>/', views.responsavel_desatribuir, name='responsavel_desatribuir'),
]