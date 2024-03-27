from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, generics, routers
from rest_framework.views import APIView

from novel_api.backend.models import Novel, Chapter, Comment, Category
from novel_api.backend.serializers import (GroupSerializer, UserSerializer,
                                           NovelSerializer, ChapterSerializer,
                                           CommentSerializer, CategorySerializer)
from novel_api.services import (NovelService, ChapterService, CommentService,
                                CategoryService)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BaseViewSet(viewsets.ModelViewSet):
    """Base viewset for listing, creating, retrieving, updating, and destroying objects."""

    permission_classes = [permissions.IsAuthenticated]
    service_class = None
    serializer_class = None

    def get_queryset(self):
        return self.service_class().get_all()

    def get_object(self):
        return self.service_class().get_by_id(self.kwargs['pk'])


class NovelViewSet(BaseViewSet):
    service_class = NovelService
    serializer_class = NovelSerializer


class ChapterViewSet(BaseViewSet):
    service_class = ChapterService
    serializer_class = ChapterSerializer


class CommentViewSet(BaseViewSet):
    service_class = CommentService
    serializer_class = CommentSerializer


class CategoryViewSet(BaseViewSet):
    service_class = CategoryService
    serializer_class = CategorySerializer
