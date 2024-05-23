from rest_framework import serializers
from sistema_gerenciador_de_tarefas_app import models

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tarefa
        fields = ['id', 'name', 'description', 'status', 'priority', 'inserted_at', 'usuario']