import hashlib

from data_acess.repository import Repository
from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Usuario
from django.shortcuts import redirect


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = hashlib.sha256(senha.encode()).hexdigest()
    usuarios = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuarios) == 0: #verificar se senha ou email incorretos
        return redirect('/auth/login/?status=1')
    elif len(usuarios) > 0: #verificar se o usuario existe
        request.session['usuario'] = usuarios[0].id
        return redirect('/home/')
    
    #usuario = [email, senha, nome]

    Repository.save_obj()
