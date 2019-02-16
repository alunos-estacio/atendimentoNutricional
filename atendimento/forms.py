from django import forms
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.helper import FormHelper
from atendimento.models import Paciente, Entrevista, Alimentos, \
    Refeicoes

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('__all__')

class EntrevistaForm(forms.ModelForm):

    class Meta:
        model = Entrevista
        fields = ('__all__')

class AlimentosForm(forms.ModelForm):

    class Meta:
        model = Alimentos
        fields = ('__all__')

class RefeicoesForm(forms.ModelForm):

    class Meta:
        model = Refeicoes
        fields = ('__all__')