from django.contrib import admin
from .models import Funcionario, Paciente, Equipe, Alimentos, Entrevista,\
    Refeicoes, Preparo
# Register your models here.


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'data_nasc', 'idade']
    search_fields = ['nome', 'cpf']

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'matricula', 'enfermaria', 'leito', 'data_nasc', 'idade']
    search_fields = ['nome', 'cpf', 'matricula']

class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    
class AlimentosAdmin(admin.ModelAdmin):
    list_display = ['nome']

class EntrevistaAdmin(admin.ModelAdmin):
    list_display = ['paciente']

class RefeicoesAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'nome', 'get_preparo', 'get_alimentos']
    search_fields = ['paciente', 'cpf']

class PreparoAdmin(admin.ModelAdmin):
    list_display = ['nome']


admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Alimentos, AlimentosAdmin)
admin.site.register(Entrevista, EntrevistaAdmin)
admin.site.register(Refeicoes, RefeicoesAdmin)
admin.site.register(Preparo, PreparoAdmin)


