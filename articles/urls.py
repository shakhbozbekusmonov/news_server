from django.urls import path
from .views import (
    CategoryApiView,
    CategoryDetailApiView,
    CategoryCreateApiView,
    CategoryUpdateApiView,
    CategoryDeleteApiView,
    ArticlesListApiView,
    ArticlesAdminListApiView,
    ArticlesCreateApiView,
    ArticlesUpdateApiView,
    ArticlesDeleteApiView,
    ArticlesDetailApiView
)


urlpatterns = [
    path('category/', CategoryApiView.as_view()),
    path('category/<int:pk>/', CategoryDetailApiView.as_view()),
    path('category/create/', CategoryCreateApiView.as_view()),
    path('category/<int:pk>/update/', CategoryUpdateApiView.as_view()),
    path('category/<int:pk>/delete/', CategoryDeleteApiView.as_view()),
    path('articles/', ArticlesListApiView.as_view()),
    path('articles/admin/', ArticlesAdminListApiView.as_view()),
    path('articles/create/', ArticlesCreateApiView.as_view()),
    path('articles/<int:pk>/update/', ArticlesUpdateApiView.as_view()),
    path('articles/<int:pk>/delete/', ArticlesDeleteApiView.as_view()),
    path('articles/<int:pk>/', ArticlesDetailApiView.as_view()),
]