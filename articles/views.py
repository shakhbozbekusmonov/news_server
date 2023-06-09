from .models import Category, Articles
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import CategorySerializer, ArticlesSerializer


class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryDetailApiView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateApiView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateApiView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteApiView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticlesListApiView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [AllowAny]


class ArticlesCreateApiView(generics.CreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class ArticlesUpdateApiView(generics.UpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class ArticlesDeleteApiView(generics.DestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class ArticlesDetailApiView(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
