from django.shortcuts import render

from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics,status,filters
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer 

class UserList(generics.ListCreateAPIView):
	
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer