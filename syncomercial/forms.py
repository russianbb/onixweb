from django import forms

from .models import Filial, RTV, Responsavel, RTV_Distribuidor, Responsavel_Distribuidor

class FilialForm(forms.ModelForm):
    class Meta:
        model = Filial
        fields = [
            'distribuidor',
            'codigo',
            'nome',
            'cnpj',
            'responsavel',
            'ddd',
            'telefone',
            'endereco',
            'cidade',
            'estado',
            'codibge',
            'latitude',
            'longitude',
        ]
        

class RtvForm(forms.ModelForm):
    class Meta:
        model = RTV
        fields = [
            'nome',
            'code_spoca',
            'email',
            'ddd1',
            'telefone1',
            'ramal1',
            'ddd2',
            'telefone2',
            'ramal2',
            'anotacao',
            'status',
        ]
        
class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = [
            'nome',
            'cargo',
            'atuacao',
            'email',
            'ddd1',
            'telefone1',
            'ramal1',
            'ddd2',
            'telefone2',
            'ramal2',
            'anotacao',
            'status',
        ]
        
        
class RTV_DistribuidorForm(forms.ModelForm):
    class Meta:
        model = RTV_Distribuidor
        fields = [
            'distribuidor',
            'RTV',
        ]
        
class Responsavel_DistribuidorForm(forms.ModelForm):
    class Meta:
        model = Responsavel_Distribuidor
        fields = [
            'distribuidor',
            'responsavel',
        ]