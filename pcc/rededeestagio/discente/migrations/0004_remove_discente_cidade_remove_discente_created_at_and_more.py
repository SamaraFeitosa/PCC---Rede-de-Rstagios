# Generated by Django 4.0.4 on 2022-06-29 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discente', '0003_remove_discente_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discente',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='discente',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='discente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='discente',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='discente',
            name='serie',
        ),
        migrations.RemoveField(
            model_name='discente',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='discente',
            name='turma',
        ),
        migrations.RemoveField(
            model_name='discente',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='discente',
            name='usuario',
        ),
    ]
