from django.db import models
from django.contrib.auth import get_user_model

class Article(models.Model):

    title           = models.CharField(max_length=30)
    content         = models.TextField()
    date_created    = models.DateField(auto_now=True)
  
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="author")

    def __str__(self):
        return self.title
    

class Comment(models.Model):

    author  = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="com_author")
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="article")

    comment         = models.CharField(max_length=150)
    date_created    = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment
    