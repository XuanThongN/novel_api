from .backend.models import Category, Novel, Chapter, Comment


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, id):
        return self.model.objects.get(id=id)

    def create(self, data):
        return self.model.objects.create(**data)

    def update(self, instance, data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)


class NovelRepository(BaseRepository):
    def __init__(self):
        super().__init__(Novel)


class ChapterRepository(BaseRepository):
    def __init__(self):
        super().__init__(Chapter)


class CommentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Comment)

    def create(self, data):  # Fix typo: create for Comment
        return Comment.objects.create(**data)
