from django.urls import path
from .views import (
    CategoryApiView,
    CategoryDetailApiView,
    ArticlesListApiView,
    ArticlesCreateApiView,
    ArticlesUpdateApiView,
    ArticlesDeleteApiView,
    ArticlesDetailApiView
)


urlpatterns = [
    path('category/', CategoryApiView.as_view()),
    path('category/<int:pk>/', CategoryDetailApiView.as_view()),
    path('articles/', ArticlesListApiView.as_view()),
    path('articles/create/', ArticlesCreateApiView.as_view()),
    path('articles/<int:pk>/update/', ArticlesUpdateApiView.as_view()),
    path('articles/<int:pk>/delete/', ArticlesDeleteApiView.as_view()),
    path('articles/<int:pk>/', ArticlesDetailApiView.as_view()),
]