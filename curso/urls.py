from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('adicionarCurso/', views.CursoAdd.as_view(), name='add_curso'),
    path('gerenciar/',views.Gerenciar.as_view(), name='gerenciar'),
    path('deletar/<int:pk>/', views.deletar, name='deletar'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('cursos/', views.Cursos.as_view(), name='cursos'),
]
