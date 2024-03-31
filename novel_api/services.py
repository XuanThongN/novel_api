import io
import os
from pathlib import Path

import imgurpython
from dotenv import load_dotenv

from .backend.ml_model import ToxicCommentClassifier
from .backend.models import Novel, Chapter, Comment
from .repositories import NovelRepository, ChapterRepository, CommentRepository, CategoryRepository
import requests


class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def create(self, data):
        return self.repository.create(data)

    def update(self, instance, data):
        return self.repository.update(instance, data)

    def delete(self, instance):
        self.repository.delete(instance)


class NovelService(BaseService):
    def __init__(self):
        super().__init__(NovelRepository())

    def get_novel_with_category(self, category_id):
        return Novel.objects.filter(category_id=category_id)


class ChapterService(BaseService):
    def __init__(self):
        super().__init__(ChapterRepository())

    def get_chapters_by_novel_id(self, novel_id):
        return Chapter.objects.filter(novel_id=novel_id)


class CommentService(BaseService):
    def __init__(self):
        super().__init__(CommentRepository())
        self.classifier = ToxicCommentClassifier()

    def predict_toxicity(self, comment_text):
        return self.classifier.predict(comment_text)

    def get_comments_by_novel_id(self, novel_id):
        return Comment.objects.filter(novel_id=novel_id)


class CategoryService(BaseService):
    def __init__(self):
        super().__init__(CategoryRepository())


class ImgurService:
    # env_path = Path('..') / '.env'
    # load_dotenv(dotenv_path=env_path)

    def __init__(self):
        self.client_id = os.environ.get('IMGUR_CLIENT_ID')
        self.client_secret = os.environ.get('IMGUR_CLIENT_SECRET')
        self.url = 'https://api.imgur.com/3/image'

    def upload_image(self, file_data):
        client = imgurpython.ImgurClient(
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        # Upload ảnh lên imgur
        image = client.upload_from_path(file_data)
        if image['link']:
            return image['link']
        else:
            print("Lỗi upload ảnh")
            return None
