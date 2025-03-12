from rest_framework import serializers
from sistema_gerenciador_de_tarefas_app import models

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tarefa
        fields = ['id', 'name', 'description', 'status', 'priority', 'inserted_at', 'usuario']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = models.Usuario(
            email=validated_data['email'],
            name=validated_data['name']                  
            )
        usuario.set_password(validated_data['password'])
        usuario.is_active = True
        usuario.save()
        return usuario