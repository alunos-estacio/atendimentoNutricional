# Generated by Django 2.0.10 on 2019-02-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0008_auto_20190215_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='refeicoes',
            name='alimentos',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to='atendimento.Alimentos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refeicoes',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to='atendimento.Paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refeicoes',
            name='preparo',
            field=models.CharField(default=1, max_length=128, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='anciedade',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Anciedade '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='bebida',
            field=models.CharField(blank=True, choices=[('Nunca', 'Nunca'), ('Socialmente', 'Socialmente'), ('Com frequência', 'Com frequência')], max_length=15, null=True, verbose_name='Faz uso de bebidas alcoólicas'),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='cansaco',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Cansaço '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='colesterol',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Colesterol '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='diabetes',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Diabetes '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='dores',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Dores diárias '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('Solteiro(a)', 'Solteiro(a)'), ('Casado(a)', 'Casado(a)'), ('Viúvo(a)', 'Viúvo(a)')], max_length=15, null=True, verbose_name='Estado civil'),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='fumante',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Fumante? '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='gastrite',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Gastrite '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='hipertencao',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Hipertenção '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='infarto',
            field=models.CharField(blank=True, choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=6, null=True, verbose_name='Infarto '),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='local',
            field=models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Trabalho', 'Trabalho'), ('Shopping', 'Shopping'), ('Outros', 'Outros')], max_length=15, null=True, verbose_name='Local das Refeições'),
        ),
        migrations.AlterField(
            model_name='refeicoes',
            name='nome',
            field=models.CharField(choices=[('Desjejum', 'Desjejum'), ('Lanche', 'Lanche'), ('Almoço', 'Almoço'), ('Lanche', 'Lanche'), ('Jantar', 'Jantar'), ('Ceia', 'Ceia')], max_length=128, verbose_name='Nome'),
        ),
    ]
