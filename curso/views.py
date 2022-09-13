from multiprocessing import context
from operator import contains
import string
from django.shortcuts import render, redirect   
from django.views import View
from .models import Curso
import unicodedata
import unidecode
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        pass

class CursoAdd(View):
    def get(self, request):
        status = request.GET.get('status')
        context = {
            'status': status,
        }
        return render(request, 'add_curso.html', context)
    def post(self, request):
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        try:
            Curso.objects.create(nome=nome, descricao=descricao)
            return redirect('cursos')
        except Exception:
            return redirect('/?status=1')

class Gerenciar(View):
    def get(self, request):
        cursos = Curso.objects.all()
        context = {
            'cursos':cursos,
        }
        return render(request, 'gerenciar.html', context)
    def post(self, request):
        pass

def deletar(request,pk):
    curso = Curso.objects.get(pk=pk)
    curso.delete()
    return redirect('gerenciar')


def editar(request, pk):
    curso = Curso.objects.get(pk=pk)
    if request.method=="GET":
        context = {
            'curso':curso
        }
        return render(request, 'editar.html', context)
    elif request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        curso.nome = nome
        curso.descricao = descricao
        curso.save()
        return redirect('gerenciar')

class Cursos(View):
    def get(self,request):
        pesquisa = request.GET.get('pesquisa')
        if pesquisa == None:
            cursos = Curso.objects.all()
        else:
            cursos = Curso.objects.all().filter(nome__icontains=pesquisa)
        context = {
            'cursos': cursos,
            'pesquisa': pesquisa,
        }
        return render(request, 'cursos.html', context)
    def post(self,request):
        pass

