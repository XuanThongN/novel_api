from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers

from novel_api.backend import views
from django.urls import path
from .backend.views import (
    NovelListCreate,
    NovelRetrieveUpdateDestroy,
    ChapterListCreate,
    ChapterRetrieveUpdateDestroy,
    CommentListCreate,
    CommentRetrieveUpdateDestroy,
    CategoryListCreate,
    CategoryRetrieveUpdateDestroy,
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('novels/', NovelListCreate.as_view(), name='novel-list-create'),
    path('novels/<int:pk>/', NovelRetrieveUpdateDestroy.as_view(), name='novel-retrieve-update-destroy'),
    path('chapters/', ChapterListCreate.as_view(), name='chapter-list-create'),
    path('chapters/<int:pk>/', ChapterRetrieveUpdateDestroy.as_view(), name='chapter-retrieve-update-destroy'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroy.as_view(), name='comment-retrieve-update-destroy'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy'),
]
