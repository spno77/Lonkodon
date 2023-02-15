from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics,status,filters
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User,Message,Connection
from .serializers import UserSerializer,MessageSerializer,ConnectionSerializer

# User serializer
class UserList(generics.ListCreateAPIView):
	
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer


# Message serializer
class MessageList(generics.ListCreateAPIView):

	serializer_class = MessageSerializer
	
	def perform_create(self, serializer):
		serializer.save(sender=self.request.user)

	def get_queryset(self):
		receiver  = self.request.user
		return Message.objects.filter(receiver=receiver)
	
class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Message.objects.all()
	serializer_class = MessageSerializer


# Connection serializer
class ConnectionList(generics.ListCreateAPIView):
	
	queryset = Connection.objects.all()
	serializer_class = ConnectionSerializer

class ConnectionDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Connection.objects.all()
	serializer_class = ConnectionSerializer
