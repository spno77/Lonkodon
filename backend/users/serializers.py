from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

#from rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = get_user_model()
		fields = ['id','username','email','firstname','lastname',
		'is_staff','phone',]

'''
class CustomRegisterSerializer(RegisterSerializer):
	firstname  = serializers.CharField()
	lastname   = serializers.CharField()
	phone      = serializers.CharField()
	
	
	def get_cleaned_data(self):
		data_dict = super().get_cleaned_data()
		data_dict['firstname']  = self.validated_data.get('firstname', '')
		data_dict['lastname']   = self.validated_data.get('lastname', '')
		data_dict['phone']      = self.validated_data.get('phone', '')
	
		return data_dict
'''