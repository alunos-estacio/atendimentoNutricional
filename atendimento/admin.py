from django.contrib import admin
from .models import Funcionario, Paciente, Equipe

# Register your models here.


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'data_nasc', 'idade']
    search_fields = ['nome', 'cpf']

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'matricula', 'quarto', 'data_nasc', 'idade']
    search_fields = ['nome', 'cpf', 'matricula']

class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']



admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Equipe, EquipeAdmin)

