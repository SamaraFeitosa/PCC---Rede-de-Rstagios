# Generated by Django 4.0.4 on 2022-06-29 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postagem',
            old_name='nome_curso',
            new_name='curso',
        ),
    ]
