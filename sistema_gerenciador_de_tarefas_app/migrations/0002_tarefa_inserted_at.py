# Generated by Django 5.0.3 on 2024-05-14 00:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_gerenciador_de_tarefas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='inserted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
