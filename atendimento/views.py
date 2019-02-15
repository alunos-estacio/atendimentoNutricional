from django.shortcuts import render, redirect
from .models import Paciente, Alimentos
from .forms import PacienteForm, EntrevistaForm, AlimentosForm

# Create your views here.

def atendimento_index(request):
    return render(request, 'index_atendimento.html')

def paciente_cadastrar(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atendimento_index')
    else:
        form = PacienteForm()
    return render(request, 'paciente_cadastrar.html', {'form': form})

def paciente_listar(request):
    paciente = Paciente.objects.all().order_by('name') 
    return render(request, 'paciente_listar.html', {'paciente':paciente})


def entrevista_criar(request):
    if request.method == "POST":
        form = EntrevistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atendimento_index')
    else:
        form = EntrevistaForm()
    return render(request, 'entrevista_create.html', {'form': form})
    
def alimento_cadastrar(request):
    if request.method == "POST":
        form = AlimentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atendimento_index')
    else:
        form = AlimentosForm()
    return render(request, 'alimento_cadastrar.html', {'form': form})

def dieta_criar(request):
    if request.method == "POST":
        form = AlimentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atendimento_index')
    else:
        form = AlimentosForm()
    return render(request, 'alimento_cadastrar.html', {'form': form})