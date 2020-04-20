from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

@login_required
def index(request):
    return render(request, 'syncomercial/index.html')


#Views relacionadas a DISTRIBUIDORES
@login_required
def distribuidores(request):
    """Lista todos os distribuidores"""
    distribuidores = Distribuidor.objects.all().order_by('razao_social')
    context = {
        'distribuidores': distribuidores,
    }
    return render(request, 'syncomercial/distribuidores.html', context)

@login_required
def distribuidor_detalhe(request, distribuidor_id):
    """Lista os detalhes de um distribuidor especifico"""
    distribuidor = Distribuidor.objects.get(id=distribuidor_id)
    filiais = distribuidor.filial_set.order_by('cnpj')
    rtvs = RTV_Distribuidor.objects.filter(distribuidor=distribuidor_id)
    responsaveis = Responsavel_Distribuidor.objects.filter(distribuidor=distribuidor_id)
    print(len(rtvs))
    context = {
        'distribuidor': distribuidor,
        'filiais': filiais,
        'rtvs': rtvs,
        'responsaveis': responsaveis,
    }
    return render(request, 'syncomercial/distribuidor_detalhe.html', context)

@login_required
def filial_detalhe(request, filial_id):
    """Lista os detalhes de uma filial em especifico"""
    filial = Filial.objects.get(id=filial_id)
    
    context = {
        'filial': filial,
    }
    return render(request, 'syncomercial/filial_detalhe.html', context)

@login_required
def filial_editar(request, filial_id):
    """Editar os dados de uma filial em especifico"""
    filial = filial = Filial.objects.get(id=filial_id)
    
    if request.method != 'POST':
        #Requisicao inicial, preenche o formulario com os dados!
        form = FilialForm(instance=filial)
    else:
        #Requisicao com edicao: validar, processar e salvar os dados.
        form = FilialForm(instance=filial, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('syncomercial:distribuidor_detalhe', distribuidor_id=filial.distribuidor_id)
        
    context = {'filial': filial, 'form': form}
    return render(request, 'syncomercial/filial_editar.html', context)

@login_required
def filial_adicionar(request, distribuidor_id):
    """Adiciona nova filial a um distribuidor em especifico"""    
    if request.method != 'POST':
        #Formulario em Branco
        form = FilialForm(initial={'distribuidor': distribuidor_id })
        
    else:
        #Formulario preenchido
        form = FilialForm(data=request.POST)
        if form.is_valid():
            #Formulario validado
            form.save()
        return redirect('syncomercial:distribuidor_detalhe', distribuidor_id = distribuidor_id)
        
    
    context = {'form': form}
    return render(request, 'syncomercial/filial_adicionar.html', context)


#Views relacionadas a RTVS
@login_required
def rtvs(request):
    """Lista todos os distribuidores"""
    rtvs = RTV.objects.all().order_by('nome')
    context = {
        'rtvs': rtvs,
    }
    return render(request, 'syncomercial/rtvs.html', context)

@login_required
def rtv_detalhe(request, rtv_id):
    rtv = RTV.objects.get(id=rtv_id)
    context = {
        'rtv': rtv
    }
    return render(request, 'syncomercial/rtv_detalhe.html', context)

@login_required
def rtv_editar(request, rtv_id):
    """Editar os dados de um rtv em especifico"""
    rtv = RTV.objects.get(id=rtv_id)
    
    if request.method != 'POST':
        #Requisicao inicial, preenche o formulario com os dados!
        form = RtvForm(instance=rtv)
    else:
        #Requisicao com edicao: validar, processar e salvar os dados.
        form = RtvForm(instance=rtv, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('syncomercial:rtv_detalhe', rtv_id=rtv_id)
        
    context = {'rtv': rtv, 'form': form}
    return render(request, 'syncomercial/rtv_editar.html', context)

@login_required
def rtv_adicionar(request):
    """Adiciona novo RTV"""
    if request.method != 'POST':
        #Formulario em Branco
        form = RtvForm()
    else:
        #Formulario preenchido
        form = RtvForm(data=request.POST)
        if form.is_valid():
            #Formulario validado
            form.save()
        return redirect('syncomercial:rtvs')
        
    
    context = {'form': form}
    return render(request, 'syncomercial/rtv_adicionar.html', context)

@login_required
def rtv_atribuir(request, distribuidor_id):
    """Cria a relacao entre RTV e Distribuidor"""
    print(f"Distribuidor ID: {distribuidor_id}")
    
    if request.method != 'POST':
        #Formulario inicial, com os dados atuais.
        print('metodo POST')
        form = RTV_DistribuidorForm(initial={'distribuidor': distribuidor_id })
    else:
        #Formulario Preenchido
        print('metodo POST')
        form = RTV_DistribuidorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('syncomercial:distribuidor_detalhe', distribuidor_id=distribuidor_id)
    
    context = {'form':form}
    return render(request, 'syncomercial/rtv_atribuir.html', context)


@login_required
def rtv_desatribuir(request, rtv_id, distribuidor_id):
    """Desatribuir/Deletar uma relacao entre RTV e Distribuidor"""
    relacao = RTV_Distribuidor.objects.get(RTV=rtv_id, distribuidor=distribuidor_id)
    relacao.delete()
    return redirect('syncomercial:distribuidor_detalhe', distribuidor_id=distribuidor_id)


#Views relacionadas a RESPONSAVEIS
@login_required
def responsaveis(request):
    """Lista todos os responsaveis"""
    responsaveis = Responsavel.objects.all().order_by('nome')
    context = {
        'responsaveis': responsaveis,
    }
    return render(request, 'syncomercial/responsaveis.html', context)

@login_required
def responsavel_detalhe(request, responsavel_id):
    responsavel = Responsavel.objects.get(id=responsavel_id)
    context = {
        'responsavel': responsavel
    }
    return render(request, 'syncomercial/responsavel_detalhe.html', context)

@login_required
def responsavel_editar(request, responsavel_id):
    """Editar os dados de um responsavel em especifico"""
    responsavel = Responsavel.objects.get(id=responsavel_id)
    
    if request.method != 'POST':
        #Requisicao inicial, preenche o formulario com os dados!
        form = ResponsavelForm(instance=responsavel)
    else:
        #Requisicao com edicao: validar, processar e salvar os dados.
        form = ResponsavelForm(instance=responsavel, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('syncomercial:responsavel_detalhe', responsavel_id=responsavel_id)
        
    context = {'responsavel': responsavel, 'form': form}
    return render(request, 'syncomercial/responsavel_editar.html', context)

@login_required
def responsavel_adicionar(request):
    
    """Adiciona novo Responsavel"""
    if request.method != 'POST':
        #Formulario em Branco
        form = ResponsavelForm()
    else:
        #Formulario preenchido
        form = ResponsavelForm(data=request.POST)
        if form.is_valid():
            #Formulario validado
            form.save()
        return redirect('syncomercial:responsaveis')
        
    
    context = {'form': form}
    return render(request, 'syncomercial/responsavel_adicionar.html', context)

@login_required
def responsavel_atribuir(request, distribuidor_id):
    """Cria a relacao entre Responsavel e Distribuidor"""
    print(f"Distribuidor ID: {distribuidor_id}")
    
    if request.method != 'POST':
        #Formulario inicial, com os dados atuais.
        print('metodo POST')
        form = Responsavel_DistribuidorForm(initial={'distribuidor': distribuidor_id })
    else:
        #Formulario Preenchido
        print('metodo POST')
        form = Responsavel_DistribuidorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('syncomercial:distribuidor_detalhe', distribuidor_id=distribuidor_id)
    
    context = {'form':form}
    return render(request, 'syncomercial/responsavel_atribuir.html', context)

@login_required
def responsavel_desatribuir(request, responsavel_id, distribuidor_id):
    """Desatribuir/Deletar uma relacao entre Responsavel e Distribuidor"""
    relacao = Responsavel_Distribuidor.objects.get(responsavel=responsavel_id, distribuidor=distribuidor_id)
    relacao.delete()
    return redirect('syncomercial:distribuidor_detalhe', distribuidor_id=distribuidor_id)