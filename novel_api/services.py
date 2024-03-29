import io
import os
from pathlib import Path

import imgurpython
from dotenv import load_dotenv

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


class ChapterService(BaseService):
    def __init__(self):
        super().__init__(ChapterRepository())


class CommentService(BaseService):
    def __init__(self):
        super().__init__(CommentRepository())


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
