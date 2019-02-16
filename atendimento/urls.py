from django.urls import path
from atendimento.views import atendimento_index, paciente_cadastrar, entrevista_criar,\
    paciente_listar, alimento_cadastrar, dieta_criar, dieta_atualizar, dieta_list, paciente_detalhar, \
    dieta_editar

urlpatterns=[
    path('', atendimento_index, name='atendimento_index'),
    path('paciente_cadastrar', paciente_cadastrar, name='paciente_cadastrar'),
    path('paciente_listar', paciente_listar, name='paciente_listar'),
    path('entrevista_criar', entrevista_criar, name='entrevista_criar'),
    path('alimento_cadastrar', alimento_cadastrar, name='alimento_cadastrar'),
    path('dieta_criar', dieta_criar, name='dieta_criar'),
    path('dieta_list', dieta_list, name='dieta_list'),
    path('paciente_detalhar/<int:pk>', paciente_detalhar, name='paciente_detalhar'),
    path('dieta_atualizar', dieta_atualizar, name='dieta_atualizar'),
    path('dieta_editar/<int:pk>', dieta_editar, name='dieta_editar'),

]

    
