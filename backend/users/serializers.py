from rest_framework import serializers
from .models import User,Message,Connection
from django.contrib.auth import get_user_model
from PIL import Image

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = get_user_model()
		fields = ['id','username','email','firstname','lastname',
		'is_staff','phone','image','employment','position']


class CustomRegisterSerializer(RegisterSerializer):
	firstname  = serializers.CharField()
	lastname   = serializers.CharField()
	phone      = serializers.CharField()
	phone      = serializers.CharField()
	image      = serializers.ImageField()
	employment = serializers.CharField()
	position   = serializers.CharField()
	
	def get_cleaned_data(self):
		data_dict = super().get_cleaned_data()
		data_dict['firstname']  = self.validated_data.get('firstname', '')
		data_dict['lastname']   = self.validated_data.get('lastname', '')
		data_dict['phone']      = self.validated_data.get('phone', '')
		data_dict['image']      = self.validated_data.get('image', '')
		data_dict['employment'] = self.validated_data.get('employment', '')
		data_dict['position']   = self.validated_data.get('position', '')

		return data_dict


class MessageSerializer(serializers.ModelSerializer):
	
	sender = UserSerializer(read_only=True)

	class Meta:
		model = Message
		fields = ['id','message','send_date','sender','receiver']



class ConnectionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Connection
		fields = ['id','source','target','is_approved','send_date']