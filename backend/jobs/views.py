from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Job
from .serializers import JobSerializer

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    


