# Generated by Django 2.0.10 on 2019-02-15 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0006_auto_20190215_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimentos',
            name='calorias',
            field=models.FloatField(blank=True, null=True, verbose_name='Calorias'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='carboidrato',
            field=models.FloatField(blank=True, null=True, verbose_name='Carboidrato'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='gordura',
            field=models.FloatField(blank=True, null=True, verbose_name='Gordura'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='proteinas',
            field=models.FloatField(blank=True, null=True, verbose_name='Proteinas'),
        ),
    ]