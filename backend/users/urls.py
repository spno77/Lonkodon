# users/urls.py

from django.urls import path,include
from . import views
from .views import UserList,UserDetail

urlpatterns = [
	path('users/',views.UserList.as_view()),
	path('users/<int:pk>/',views.UserDetail.as_view()),
]