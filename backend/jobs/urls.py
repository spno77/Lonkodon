# jobs/urls.py

from django.urls import path,include
from . import views
from .views import JobList,JobDetail

urlpatterns = [
	path('jobs/',views.JobList.as_view()),
	path('jobs/<int:pk>/',views.JobDetail.as_view()),
]