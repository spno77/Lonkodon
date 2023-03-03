# articles/urls.py

from django.urls import path,include
from . import views

urlpatterns = [
	path('articles/',views.ArticleList.as_view()),
	path('articles/<int:pk>/',views.ArticleDetail.as_view()),
	
    path('comments/',views.CommentList.as_view()),
	path('comments/<int:pk>/',views.CommentDetail.as_view()),
]
