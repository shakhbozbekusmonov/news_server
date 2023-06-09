from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Articles(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    titleUz = models.CharField(max_length=250)
    titleRu = models.CharField(max_length=250)
    titleEn = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    bodyUz = models.TextField()
    bodyRu = models.TextField()
    bodyEn = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.titleUz

