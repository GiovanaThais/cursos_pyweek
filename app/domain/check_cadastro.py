import hashlib

from data_acess.repository import Repository
from django.shortcuts import render
from django.http import HttpResponse
from app.data_acess.repository import Repository
from usuarios.models import Usuario
from django.shortcuts import redirect


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    usuario = Usuario.objects.filter(email = email)

    if len(usuario) > 0: #verificar se o user ja existe
        return redirect('/auth/cadastro/?status=1')
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0: #verifica se foi deixado campo em branco usando strip
        return redirect('/auth/cadastro/?status=2')
    
    if len(senha) < 8 or len(senha) > 12 : #verificar se senha tem no minimo 8 digitos 
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = hashlib.sha256(senha.encode()).hexdigest() #não mostrar senha no admin,retornar hash da senha
        usuario = Usuario(nome = nome,
                        email = email,
                        senha = senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')
    

def cria_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    Repository.save_obj()
