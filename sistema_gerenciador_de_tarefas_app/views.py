from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from sistema_gerenciador_de_tarefas_app import models
# Create your views here.

def listar_tarefas(request):
    items = models.Tarefa.objects.all()
    lista_de_tarefas =  [item.to_dict() for item in items]
    return JsonResponse(lista_de_tarefas, safe=False)

def buscar_tarefa_pelo_id(request, task_id):
    item = models.Tarefa.objects.get(pk=task_id)
    return JsonResponse(item.to_dict())


@csrf_exempt
def criar_tarefa(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tarefa = models.Tarefa.objects.create(**data)
        return JsonResponse(tarefa.to_dict())
    else:
        return JsonResponse({"mensagem": "Método não permitido"}, status=405)


@csrf_exempt
def editar_tarefa(request, task_id):
    if request.method == 'PUT':
        dados = json.loads(request.body.decode('utf-8'))
        
        try:
            item = models.Tarefa.objects.get(pk=task_id)
            for key, value in dados.items():
                setattr(item, key, value)
            item.save()
            return JsonResponse(item.to_dict())
        
        except models.Tarefa.DoesNotExist:
            return JsonResponse({'error': 'Tarefa não encontrada'}, status=404)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)
