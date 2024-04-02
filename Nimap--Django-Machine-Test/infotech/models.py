from django.db import models
from django.contrib.auth.models import User

class Clients(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_clients')
    updated_by = models.DateField()

class Project(models.Model):
    projects = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    created_at = models.DateField()
    users = models.ManyToManyField(User, related_name='projects', verbose_name='Assigned Users')
