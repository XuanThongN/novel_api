from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Category, Novel, Chapter, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# Category
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    # Kiểm tra tên category đã tồn tại chưa
    def validate_name(self, value):
        if self.instance is None:  # Kiểm tra xem có phải là tạo mới hay không
            if Category.objects.filter(name=value).exists():
                raise serializers.ValidationError("Category này đã tồn tại trên hệ thống.")
            return value


# Novel
class NovelSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    chapters_count = serializers.SerializerMethodField()

    class Meta:
        model = Novel
        fields = ['url', 'id', 'title', 'author', 'image_path', 'category', 'description', 'image_url',
                  'chapters_count']

    # Kiểm tra tên novel đã tồn tại chưa
    def validate_title(self, value):
        if self.instance is None:  # Kiểm tra xem có phải là tạo mới hay không
            if Novel.objects.filter(title=value).exists():
                raise serializers.ValidationError("Novel này đã tồn tại trên hệ thống.")
        return value

    # Lấy tất cả các chapter của novel
    def get_chapters_count(self, obj):
        return obj.chapters.count()

    # Lấy tất cả các comment của novel (chỉ lấy comment của novel đó)
    def get_comments(self, obj):
        return obj.comments.filter(novel_id=obj.id)


# Chapter
class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    novel = serializers.PrimaryKeyRelatedField(queryset=Novel.objects.all())

    class Meta:
        model = Chapter
        fields = ['url', 'id', 'title', 'content', 'novel']

    # Kiểm tra tên chapter đã tồn tại chưa
    def validate_title(self, value):
        if self.instance is None:  # Kiểm tra xem có phải là tạo mới hay không
            if Chapter.objects.filter(title=value).exists():
                raise serializers.ValidationError("Chapter này đã tồn tại trên hệ thống.")
            return value


#  Comment
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    novel = serializers.PrimaryKeyRelatedField(queryset=Novel.objects.all())

    class Meta:
        model = Comment
        fields = ['url', 'id', 'text', 'user', 'novel', 'created_at']

    def create(self, validated_data):
        # Get the user from the request
        user = self.context['request'].user
        # Create and return a new Comment instance, associating it with the user
        return Comment.objects.create(user=user, **validated_data)


# Đăng nhập
class UserTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    name = serializers.CharField(source='user.first_name' + ' ' + 'user.last_name')


# Đăng ký tài khoản
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # Kiểm tra username và email đã tồn tại chưa
    def validate_username(self, value):
        if self.instance is None:  # Kiểm tra xem có phải là tạo mới hay không
            if User.objects.filter(username=value).exists():
                raise serializers.ValidationError("Username này đã tồn tại trên hệ thống.")
            return value

    def validate_email(self, value):
        if self.instance is None:  # Kiểm tra xem có phải là tạo mới hay không
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("Email này đã tồn tại trên hệ thống.")
            return value

    # Tạo tài khoản
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
