from rest_framework           import serializers

from .models                  import Article,Comment
from django.contrib.auth      import get_user_model
from users.serializers        import UserSerializer

class CommentSerializer(serializers.ModelSerializer):

	author = UserSerializer(read_only=True)
	article = serializers.PrimaryKeyRelatedField(source='article.title',queryset=Article.objects.all())

	class Meta:
		model  = Comment
		fields = ['id','comment','date_created','author','article']


class ArticleSerializer(serializers.ModelSerializer):

	author   = UserSerializer(read_only=True)
	comments = CommentSerializer(read_only=True,many=True)

	class Meta:
		model = Article
		fields = ['id','title','content','date_created','comments','author']
