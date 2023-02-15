from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Job,Application
from .serializers import JobSerializer,ApplicationSerializer

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ApplicationList(generics.ListCreateAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer

	def perform_create(self, serializer):
		pk = self.request.data['job']
		job = Job.objects.get(pk=pk)
		serializer.save(author=self.request.user,job=job)

	def perform_update(self,serializer):
		serializer.save(author=self.request.user)

class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer


