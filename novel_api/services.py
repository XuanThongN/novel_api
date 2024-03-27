from .repositories import NovelRepository, ChapterRepository, CommentRepository, CategoryRepository


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
