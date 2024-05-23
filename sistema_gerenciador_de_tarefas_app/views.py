from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sistema_gerenciador_de_tarefas_app import models
from sistema_gerenciador_de_tarefas_app.serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = models.Tarefa.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = TarefaSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = self.queryset.get(pk=pk)
        return Response(item.to_dict())

    def create(self, request):
        data = request.data
        tarefa = models.Tarefa.objects.create(**data)
        return Response(tarefa.to_dict())

    def update(self, request, pk=None):
        item = self.queryset.get(pk=pk)
        for key, value in request.data.items():
            setattr(item, key, value)
        item.save()
        return Response(item.to_dict())

    def destroy(self, request, pk=None):
        item = self.queryset.get(pk=pk)
        item.delete()
        return Response({'mensagem': 'Tarefa deletada com sucesso'})