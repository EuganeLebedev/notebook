from django.db import models

# Create your models here.


class Post(models.Model):
    post_content = models.TextField(blank=False)


class Category(models.Model):
    category_name = models.CharField(blank=False, max_length=255)
