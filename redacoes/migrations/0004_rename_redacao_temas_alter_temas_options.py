# Generated by Django 4.2.2 on 2023-07-12 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redacoes', '0003_redacao_imagem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Redacao',
            new_name='Temas',
        ),
        migrations.AlterModelOptions(
            name='temas',
            options={'verbose_name': 'Tema', 'verbose_name_plural': 'Temas'},
        ),
    ]
