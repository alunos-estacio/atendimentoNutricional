from django.urls import path
from atendimento.views import atendimento_index, paciente_cadastrar, entrevista_criar, paciente_listar, alimento_cadastrar

urlpatterns=[
    path('', atendimento_index, name='atendimento_index'),
    path('paciente_cadastrar', paciente_cadastrar, name='paciente_cadastrar'),
    path('paciente_listar', paciente_listar, name='paciente_listar'),
    path('entrevista_criar', entrevista_criar, name='entrevista_criar'),
    path('alimento_cadastrar', alimento_cadastrar, name='alimento_cadastrar'),

#corrigir problema de direcionamento
]

    
