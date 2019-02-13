from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from atendimento.models import Paciente
from django.urls import reverse_lazy
from atendimento.forms import PacienteForm

# Create your views here.

def index(request):
    return render(request, "index.html")

class PacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "cadastrar_paciente.html"

    def get_sucess_url(self):
        return reverse_lazy('index')