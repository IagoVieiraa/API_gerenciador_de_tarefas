from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from sistema_gerenciador_de_tarefas_app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'tarefas', views.TarefaViewSet, basename='tarefas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registro/', views.RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]