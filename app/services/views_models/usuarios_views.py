from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Usuario
from django.shortcuts import redirect
import hashlib


def cadastro(request): 
    #if request.session.get('usuario'):
        #return redirect('/home/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def sair(request):
    request.session.flush() #remove tudo do usuario no sistema
    return redirect('/auth/login/')
