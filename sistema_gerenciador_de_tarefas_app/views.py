from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from sistema_gerenciador_de_tarefas_app import models
from sistema_gerenciador_de_tarefas_app.serializers import TarefaSerializer, UsuarioSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            usuario = models.Usuario.objects.get(email=email)
            if usuario.is_active and usuario.check_password(password):
                refresh = RefreshToken.for_user(usuario)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        except models.Usuario.DoesNotExist:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'mensagem': 'Deslogado com sucesso'})

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = models.Tarefa.objects.all()
    permission_classes = (IsAuthenticated,)
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