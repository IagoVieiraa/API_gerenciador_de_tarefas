from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    groups = models.ManyToManyField('auth.Group', related_name='usuario_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='usuario_permissions', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def check_password(self, raw_password):
        return super().check_password(raw_password)
    

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=244)
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    inserted_at = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'inserted_at': self.inserted_at
        }        