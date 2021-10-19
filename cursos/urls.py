from django.urls import path
from . import views
from .viewsets import CursosAPIView, ListarCursosAPIView, ListarAulasAPIView, AulasAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cursos', ListarCursosAPIView, CursosAPIView)
router.register('opcoes', ListarAulasAPIView, AulasAPIView)

urlpatterns = [
    path('', views.home, name = 'home'),
    path('curso/<int:id>', views.curso, name = 'curso'),
    path('aula/<int:id>', views.aula, name = 'aula'),
    path('comentarios/', views.comentarios, name = 'comentarios'),
    path('processa_avaliacao/', views.processa_avaliacao, name = 'processa_avaliacao'),

    #api
    path("cursos/", ListarCursosAPIView.as_view(), name='cursos_api'),
    path("cursos/<int:pk>/", CursosAPIView.as_view(), name='curso_api'),
    path("aulas/", ListarAulasAPIView.as_view(), name='aulas_api'),
    path("aulas/<int:pk>/", AulasAPIView.as_view(), name='aula_api'),
]
