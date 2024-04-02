from rest_framework import serializers
from .models import User,Clients,Project

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username')
        
class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','project_name','projects','created_by','created_at')
        
class Clientserializer(serializers.ModelSerializer):
    projects=Projectserializer(many=True,read_only=True)
    class Meta:
        model=Clients
        fields=('id','client_name','created_by','projects','created_at','updated_by',)
        
