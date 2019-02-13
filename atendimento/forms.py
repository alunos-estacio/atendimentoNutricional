from django import forms
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.helper import FormHelper
from atendimento.models import Paciente

class PacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                'nome',
                'cpf',
                'data_nasc',
                'idade', 
                'matricula', 
                'quarto',
                Submit('salvar', 'Salvar', css_class='btn btn-success')
            ),
        )
    class Meta:
        model = Paciente
        fields = ('nome',
                'cpf',
                'data_nasc',
                'idade', 
                'matricula', 
                'quarto',)
