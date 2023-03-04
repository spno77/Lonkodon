# users/urls.py

from django.urls import path,include
from . import views

urlpatterns = [
	# User paths
	path('users/',views.UserList.as_view()),
	path('users/<int:pk>/',views.UserDetail.as_view()),
	
	# Message paths
	path('messages/',views.MessageList.as_view()),
	path('messages/<int:pk>/',views.MessageDetail.as_view()),
	
	# Connection paths
	path('connections/',views.ConnectionList.as_view()),
	path('conn_requests/',views.ConnectionRequestList.as_view()),
	path('connections/<int:pk>/',views.ConnectionDetail.as_view()),
	path('connections/find/',views.ConnectionFindList.as_view()),
]