from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from .viewsets import UsuarioAPIView, ListarUsuarioAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('usuario', ListarUsuarioAPIView, UsuarioAPIView)

urlpatterns = [
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('login/', views.login, name = 'login'),
    path('valida_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    path('valida_login/', views.valida_login, name = 'valida_login'),
    path('sair/', views.sair, name = 'sair'),

    #API 
    path('usuarios/', ListarUsuarioAPIView.as_view(), name='usuarios_api'),
    path('usuario/<int:pk>/', UsuarioAPIView.as_view(), name='usuario_api'),
]
