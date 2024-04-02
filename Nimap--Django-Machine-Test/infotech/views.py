from django.http import JsonResponse
from django.shortcuts import render
from .serializer import Userserializer, Clientserializer, Projectserializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Clients, Project

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = Clientserializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = Projectserializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update_users(self, request, *args, **kwargs):
        instance = self.get_object()
        user_ids = request.data.get('users', [])
        instance.users.set(user_ids)
        return Response({'message': 'Users assigned successfully'})
