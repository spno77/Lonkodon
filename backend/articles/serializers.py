from rest_framework           import serializers

from .models                  import Article,Comment
from django.contrib.auth      import get_user_model
from users.serializers        import UserSerializer

class CommentSerializer(serializers.ModelSerializer):

	author = UserSerializer(read_only=True)
	article = serializers.PrimaryKeyRelatedField(source='article.title',queryset=Article.objects.all())

	class Meta:
		model  = Comment
		fields = ['id','commnent','date_created',]


class ArticleSerializer(serializers.ModelSerializer):

	author   = UserSerializer(read_only=True)
	comments = CommentSerializer(many=True,read_only=True)

	class Meta:
		model = Article
		fields = ['id','title','content','date_created','author','comments',]
