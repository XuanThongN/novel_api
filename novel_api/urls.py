from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers

# from novel_api.backend import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from novel_api.backend.views import UserViewSet, GroupViewSet, NovelViewSet, ChapterViewSet, CommentViewSet, \
    CategoryViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'novels', NovelViewSet, basename='novel')
router.register(r'chapters', ChapterViewSet, basename='chapter')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'categories', CategoryViewSet, basename='category')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), //Tắt chức năng login
    path('admin/', admin.site.urls),
]
