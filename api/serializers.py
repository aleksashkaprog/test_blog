from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_recursive.fields import RecursiveField
from .models import Article, Comment


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'articles', 'comments']


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    children = RecursiveField(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'article', 'parent', 'created_date', 'author', 'children']


