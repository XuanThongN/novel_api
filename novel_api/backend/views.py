from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics

from novel_api.backend.models import Novel, Chapter, Comment, Category
from novel_api.backend.serializers import GroupSerializer, UserSerializer, NovelSerializer, ChapterSerializer, \
    CommentSerializer, CategorySerializer
from novel_api.services import NovelService, ChapterService, CommentService, CategoryService


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


class NovelListCreate(generics.ListCreateAPIView):
    queryset = NovelService.get_all()
    serializer_class = NovelSerializer


class NovelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer


class ChapterListCreate(generics.ListCreateAPIView):
    queryset = ChapterService.get_all()
    serializer_class = ChapterSerializer


class ChapterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class CommentListCreate(generics.ListCreateAPIView):
    queryset = CommentService.get_all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = CategoryService.get_all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
