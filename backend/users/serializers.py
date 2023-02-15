from rest_framework import serializers
from .models import User,Message,Connection
from django.contrib.auth import get_user_model
from PIL import Image

#from rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = get_user_model()
		fields = ['id','username','email','firstname','lastname',
		'is_staff','phone','image']

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

class MessageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Message
		fields = ['id','username','message','send_date','receiver']



class ConnectionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Connection
		fields = ['id','source','target','is_approved','send_date']