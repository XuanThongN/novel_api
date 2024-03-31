import os
from pathlib import Path

from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, generics, routers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from novel_api.backend import serializers
from novel_api.backend.serializers import (GroupSerializer, UserSerializer,
                                           NovelSerializer, ChapterSerializer,
                                           CommentSerializer, CategorySerializer)
from novel_api.services import (NovelService, ChapterService, CommentService,
                                CategoryService, ImgurService)


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

    def perform_create(self, serializer):
        novel = serializer.save()
        self.upload_image(novel)

    def perform_update(self, serializer):
        novel = serializer.save()
        self.upload_image(novel)

    def upload_image(self, novel):
        image_data = self.request.FILES.get('image_path')
        if image_data:
            imgur_service = ImgurService()
            file_data = Path('.') / 'novel_images' / image_data.name
            image_url = imgur_service.upload_image(file_data)
            if image_url:
                novel.image_url = image_url
                novel.image_path = None
                novel.save()
                #  xoá file với đường dẫn file_data
                os.remove(file_data)


class ChapterViewSet(BaseViewSet):
    service_class = ChapterService
    serializer_class = ChapterSerializer


class CommentViewSet(BaseViewSet):
    service_class = CommentService
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        comment_text = self.request.data['text']
        is_toxic = self.service_class().predict_toxicity(comment_text)
        if not is_toxic:
            serializer.save()
            return Response({
                'success': True,
                'message': 'Bình luận đã được lưu thành công.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError("Bình luận chứa nội dung độc hại hoặc liên quan đến chính trị.")


class CategoryViewSet(BaseViewSet):
    service_class = CategoryService
    serializer_class = CategorySerializer
