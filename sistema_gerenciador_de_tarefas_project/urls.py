"""sistema_gerenciador_de_tarefas_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from sistema_gerenciador_de_tarefas_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('tarefas/criar', views.criar_tarefa, name='criar_tarefa')
]
