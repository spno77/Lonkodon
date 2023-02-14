# users/urls.py

from django.urls import path,include
from . import views
from .views import UserList,UserDetail,MessageList,MessageDetail

urlpatterns = [
	path('users/',views.UserList.as_view()),
	path('users/<int:pk>/',views.UserDetail.as_view()),
	path('messages/',views.MessageList.as_view()),
	path('messages/<int:pk>/',views.MessageDetail.as_view()),
]