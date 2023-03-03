from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Article,Comment
from .serializers import ArticleSerializer,CommentSerializer

# Article views
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self,serializer):
        serializer.save(author= self.request.user)
    
    def perform_update(self,serilizer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# Comment views
class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self,serializer):
        pk = self.request.data['article']
        article = Article.objects.get(pk=pk)
        serializer.save(author=self.request.user,article=article)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
