from django.db import models

# Create your models here.
class Tarefa(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=244)
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
        }        