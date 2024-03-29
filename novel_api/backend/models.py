from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Novel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(default='No description provided.')
    image_path = models.ImageField(upload_to='novel_images/', blank=True)  # Thêm trường image_path
    image_url = models.URLField(max_length=200, blank=True)  # Thêm trường image_url
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='novels')

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text
