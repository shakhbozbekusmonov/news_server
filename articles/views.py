from django.db.models import Q
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
    serializer_class = ArticlesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Articles.objects.filter(status="PB")
        search_query = self.request.query_params.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(titleUz__icontains=search_query) |
                Q(titleRu__icontains=search_query) |
                Q(titleEn__icontains=search_query)
            )
        return queryset


class ArticlesAdminListApiView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


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
