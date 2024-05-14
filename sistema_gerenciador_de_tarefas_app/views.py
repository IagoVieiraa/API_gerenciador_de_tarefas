from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.views.decorators.csrf import csrf_exempt
from sistema_gerenciador_de_tarefas_app import models
# Create your views here.

def listar_tarefas(request):
    items = models.Tarefa.objects.all()
    lista_de_tarefas =  [item.to_dict() for item in items]
    tarefas_json = json.dumps(lista_de_tarefas, cls=DjangoJSONEncoder)
    return HttpResponse(json.dumps(tarefas_json), content_type='application/json')

@csrf_exempt
def criar_tarefa(request):
    if request.method == 'POST':
        dados = {
            'name' : request.POST.get('name'),
            'description' : request.POST.get('description'),
            'status' : request.POST.get('status'),
            'priority' : request.POST.get('priority')
        }
        models.Tarefa.objects.create(**dados)
    return HttpResponse(json.dumps({"status": "success"}), content_type='application/json')
