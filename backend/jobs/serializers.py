from rest_framework import serializers
from .models import Job
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    
    poster = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id','title','date_created','level','desciption','experience']