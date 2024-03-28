from django.contrib import admin
from django.contrib.auth.models import Group

from novel_api.backend.models import Category, Novel, Chapter, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Comment)
