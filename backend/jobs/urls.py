# jobs/urls.py

from django.urls import path,include
from . import views

urlpatterns = [
	path('jobs/',views.JobList.as_view()),
	path('jobs/<int:pk>/',views.JobDetail.as_view()),
	path('applications/',views.ApplicationList.as_view()),
	path('applications/<int:pk>/',views.ApplicationDetail.as_view()),
]