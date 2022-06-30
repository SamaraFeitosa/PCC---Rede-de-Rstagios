# Generated by Django 4.0.4 on 2022-06-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discente', '0004_remove_discente_cidade_remove_discente_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discente',
            name='nome',
            field=models.CharField(max_length=50, null=True, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='discente',
            name='usuario',
            field=models.CharField(max_length=20, null=True, verbose_name='Usuário'),
        ),
    ]
