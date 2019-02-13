from django.urls import path
from atendimento.views import PacienteCreate, index

urlpatterns=[
    path('', index, name='index'),
        path('cadastrar-paciente/', PacienteCreate.as_view(),name='cadastrar_paciente'),

]


