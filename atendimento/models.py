from django.db import models
from django.forms import ModelForm

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=128, verbose_name='Nome', null=False, blank=False)
    cpf = models.CharField(verbose_name='CPF', max_length=128, null=False, blank=False)
    data_nasc = models.DateField(verbose_name='Data de Nascimento', null=False, blank=False)
    idade = models.IntegerField(verbose_name='Idade', null=False, blank=False)

    class Meta: 
        abstract=True
    

class Equipe(models.Model):
    nome = models.CharField(max_length=12, verbose_name='Nome', null=False, blank=False)
    descricao = models.CharField(max_length=128,verbose_name='Descrição da Atividade', null=False, blank=False)
    
    class Meta: 
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
    
    def __str__(self):
        return '%s' % (self.nome) 


class Funcionario(Pessoa):
    matricula = models.CharField(max_length=12, verbose_name='Matricula', null=False, blank=False)
    função = models.CharField(max_length=128, verbose_name='Função', null=False, blank=False)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return '%s' % (self.nome) 


class Paciente(Pessoa):

    matricula = models.CharField(max_length=12, verbose_name='Matricula', null=False, blank=False)
    quarto = models.CharField(max_length=128,verbose_name='Quarto', null=False, blank=False)
    
    class Meta: 
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
    
    def __str__(self):
        return '%s' % (self.nome) 

ESTADO_CIVIL_CHOICES = (
    ('----', '----'),
    ('Solteiro(a)', 'Solteiro(a)'),
    ('Casado(a)', 'Casado(a)'),
    ('Viúvo(a)', 'Viúvo(a)'),
)

SIM_NAO_CHOICES=(
    ('----', '----'),
    ('Não', 'Não'),
    ('Sim', 'Sim'),
)

LOCAL_CHOICES=(
    ('----', '----'),
    ('Casa', 'Casa'),
    ('Trabalho', 'Trabalho'),
    ('Shopping', 'Shopping'),
    ('Outros', 'Outros'),
)

BEBIDA_CHOICES=(
    ('----', '----'),
    ('Nunca', 'Nunca'),
    ('Socialmente', 'Socialmente'),
    ('Com frequência', 'Com frequência'),
)

class Entrevista(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cod_ficha = models.CharField(max_length=12, verbose_name='Cód. Ficha', null=False, blank=False)
    motivo = models.CharField(max_length=300,verbose_name='Motivo da Consulta', null=True, blank=True)
    #historico familiar
    estado_civil = models.CharField(max_length=15,verbose_name='Motivo da Consulta', choices = ESTADO_CIVIL_CHOICES, null=True, blank=True)
    profissao = models.CharField(max_length=128, verbose_name='Profissão', null=True, blank=True)
    local= models.CharField(max_length=15, verbose_name='Local das Refeições', choices = LOCAL_CHOICES, null=True, blank=True)
    fumante = models.CharField(max_length=6,verbose_name='Fumante? ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    bebida= models.CharField(max_length=15, verbose_name='Faz uso de bebidas alcoólicas', choices = BEBIDA_CHOICES, null=True, blank=True)
    #historico clinico
    diabetes = models.CharField(max_length=6,verbose_name='Diabetes ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    colesterol = models.CharField(max_length=6,verbose_name='Colesterol ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    anciedade = models.CharField(max_length=6,verbose_name='Anciedade ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    infarto = models.CharField(max_length=6,verbose_name='Infarto ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    hipertencao = models.CharField(max_length=6,verbose_name='Hipertenção ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    cansaco = models.CharField(max_length=6,verbose_name='Cansaço ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    gastrite = models.CharField(max_length=6,verbose_name='Gastrite ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    dores = models.CharField(max_length=6,verbose_name='Dores diárias ', choices = SIM_NAO_CHOICES, null=True, blank=True)
    diagnostico = models.CharField(max_length=300, verbose_name='Diagnostico Final ', null=True, blank=True)

    class Meta: 
        verbose_name = 'Entrevista'
        verbose_name_plural = 'Entrevistas'
    
    def __str__(self):
        return '%s' % (self.paciente.nome) 