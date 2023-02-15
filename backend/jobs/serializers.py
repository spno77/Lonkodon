from rest_framework import serializers
from .models import Job,Application
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    
    poster = UserSerializer(read_only=True)
    #applications = ApplicationSerializer(many=True,read_only=True)

    class Meta:
        model = Job
        fields = ['id','title','date_created','level','description',
                    'experience','poster',]


class ApplicationSerializer(serializers.ModelSerializer):

    applicant = UserSerializer(read_only=True)
    job       = JobSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id','date_applied','applicant','job']