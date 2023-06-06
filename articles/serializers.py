from rest_framework import serializers
from .models import Category, Articles


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articles
        fields = ['id', 'titleUz', 'titleRu', 'titleEn', 'slug', 'bodyUz', 'bodyRu', 'bodyEn', 'image', 'category', 'publish_time', 'created_time', 'updated_time', 'status']

