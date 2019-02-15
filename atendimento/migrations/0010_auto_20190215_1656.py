# Generated by Django 2.0.10 on 2019-02-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0009_auto_20190215_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refeicoes',
            name='alimentos',
        ),
        migrations.AddField(
            model_name='refeicoes',
            name='alimentos',
            field=models.ManyToManyField(to='atendimento.Alimentos'),
        ),
        migrations.AlterField(
            model_name='refeicoes',
            name='nome',
            field=models.CharField(choices=[('Desjejum', 'Desjejum'), ('Lanche', 'Lanche'), ('Almoço', 'Almoço'), ('Lanche', 'Lanche'), ('Jantar', 'Jantar'), ('Ceia', 'Ceia')], max_length=128, verbose_name='Refeição'),
        ),
    ]
