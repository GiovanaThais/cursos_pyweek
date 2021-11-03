import hashlib

from data_acess.repository import Repository
from django.shortcuts import render
from django.http import HttpResponse
from cursos.models import Cursos, NotasAulas, Aulas
from django.shortcuts import redirect



def processa_avaliacao(request):
    if request.session.get('usuario'):

        avaliacao = request.POST.get('avaliacao')
        aula_id = request.POST.get('aula_id')
        
        usuario_id = request.session.get('usuario')

        usuario_avaliou = NotasAulas.objects.filter(aula_id = aula_id).filter(usuario_id = usuario_id)

        if not usuario_avaliou:
            nota_aulas = NotasAulas(aula_id = aula_id,
                                    nota = avaliacao,
                                    usuario_id = usuario_id,
                                    )
            nota_aulas.save()
            return redirect(f'/home/aula/{aula_id}')
        else:
            return redirect('/auth/login/')

    else:
        return redirect('/auth/login/')
    

def cria_curso(request, id): 
    if request.session.get('usuario'):
        aulas = Aulas.objects.filter(curso = id)
        request_usuario = request.session.get('usuario')
        return render(request, 'curso.html', {'aulas': aulas, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')
    
    Repository.save_obj()
    