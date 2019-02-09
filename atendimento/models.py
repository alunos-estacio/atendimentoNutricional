from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=128, verbose_name='Nome', null=False, blank=False)
    cpf = models.IntegerField(verbose_name='CPF', null=False, blank=False)
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
