# Generated by Django 2.0.10 on 2019-02-16 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0013_auto_20190215_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='quarto',
        ),
        migrations.AddField(
            model_name='paciente',
            name='enfermaria',
            field=models.CharField(choices=[('Enfermaria 01', 'Enfermaria 01'), ('Enfermaria 02', 'Enfermaria 02'), ('Enfermaria 03', 'Enfermaria 03'), ('Enfermaria 04', 'Enfermaria 04')], default=1, max_length=128, verbose_name='Enfermaria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='leito',
            field=models.CharField(choices=[('Enfermaria 01', 'Enfermaria 01'), ('Enfermaria 02', 'Enfermaria 02'), ('Enfermaria 03', 'Enfermaria 03'), ('Enfermaria 04', 'Enfermaria 04')], default=1, max_length=128, verbose_name='Leito'),
            preserve_default=False,
        ),
    ]
