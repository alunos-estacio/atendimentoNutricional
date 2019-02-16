from django.shortcuts import render, redirect
from .models import Paciente, Alimentos, Refeicoes
from .forms import PacienteForm, EntrevistaForm, AlimentosForm, \
    RefeicoesForm

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
        form = RefeicoesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atendimento_index')
    else:
        form = RefeicoesForm()
    return render(request, 'alimento_cadastrar.html', {'form': form})


def dieta_atualizar(request):
    pacientes = Paciente.objects.all()
    refeicoes = Refeicoes.objects.all()
    return render(request, 'dieta_atualizar.html', {'pacientes': pacientes, 'refeicoes':refeicoes})


def dieta_editar(request, pk, queryset=None):
    paciente = Paciente.objects.get(pk=pk)
    refeicoes = Refeicoes.objects.filter(paciente=paciente)    
    if request.method == "POST":
        form = RefeicoesForm(request.POST, instance=refeicoes)
        if form.is_valid():
            form.save()
            return redirect('atendimento_index') 
    else:
        form = RefeicoesForm(instance=refeicoes)
    return render(request, 'alimento_cadastrar.html', {'form': form})


def dieta_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'dietas_listagem.html', {'pacientes': pacientes})


def paciente_detalhar(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    refeicoes = Refeicoes.objects.filter(paciente=paciente)
    return render(request, 'paciente_detalhar.html', {'paciente': paciente, 'refeicoes':refeicoes})