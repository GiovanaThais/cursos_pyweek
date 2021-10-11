from django.shortcuts import render
from .models import Cursos, Aulas
from django.shortcuts import redirect

def home(request): #validando para apenas quem ter acesso ao home ser quem tiver logado
    if request.session.get('usuario'):
        cursos = Cursos.objects.all()
        request_usuario = request.session.get('usuario')
        return render(request, 'home.html', {'cursos': cursos, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')
    #emitir alerta ao tentar acesso sem login

def curso(request, id): 
    if request.session.get('usuario'):
        aulas = Aulas.objects.filter(curso = id)
        request_usuario = request.session.get('usuario')
        return render(request, 'curso.html', {'aulas': aulas, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')

def aula(request, id):
    if request.session.get('usuario'):
        aula = Aulas.objects.get(id = id)
        return render(request, 'aula.html', {'aula': aula})
    else:
        return redirect('/auth/login/?status=2')