from django import forms
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.helper import FormHelper
from atendimento.models import Paciente, Entrevista



class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('__all__')

class EntrevistaForm(forms.ModelForm):

    class Meta:
        model = Entrevista
        fields = ('__all__')