from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
import hashlib

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/home/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def sair(request):
    request.session.flush() #remove tudo do usuario no sistema
    return redirect('/auth/login/')

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
# Create your views here.
