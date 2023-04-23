

from rest_framework.serializers import ModelSerializer

from pages.models import IjtimoiyTarmoqlar

from articles.models import (
    Article, ArticleColumn,Journal, Post
)

class IjtimoiyTarmoqlarSerializer(ModelSerializer):
    class Meta:
        model = IjtimoiyTarmoqlar
        fields = [
            'name', 'icon'
        ]

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']
        depth = True


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 'title', 'file', 'approved_date_time',
            'description', 'first_name', 'last_name', 'journal',
            'column'
        ]
        depth = True

class ArticleColumnSerializer(ModelSerializer):
    class Meta:
        model = ArticleColumn
        fields = '__all__'


class JournalSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
