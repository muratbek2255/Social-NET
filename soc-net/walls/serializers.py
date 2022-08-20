from rest_framework import serializers

from viewsets.serializers import FilterCommentListSerializer, RecursiveSerializer
from walls.models import Post, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'post', 'text', 'parent')


class ListCommentSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='customuser.username')

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('id', 'created_date', 'user', 'update_date', 'published', 'deleted', 'user', 'post', 'text', 'parent', 'children')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='customuser.username')
    comments = ListCommentSerializer(many=True, read_only=True)
    views_count = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'comments', 'created_at', 'views_count')


class ListPostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='customuser.username')

    class Meta:
        model = Post
        fields = ('id', 'user', 'text', 'created_at', 'views_count', 'comments_count')
