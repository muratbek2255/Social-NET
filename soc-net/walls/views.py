from rest_framework import permissions, generics

from viewsets.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy
from viewsets.permissions import IsMemberGroup, IsAuthorEntry, IsAuthorComment, IsAuthor
from walls.models import Post, Comment
from walls.serializers import CreateCommentSerializer, ListCommentSerializer, PostSerializer, ListPostSerializer


class PostView(CreateRetrieveUpdateDestroy):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.select_related('customuser').all()
    serializer_class = PostSerializer
    permission_classes_by_action = {
        'get': [permissions.AllowAny],
        'update': [IsAuthor],
        'destroy': [IsAuthor],
    }

    def perform_create(self, serializer):
        return serializer.save(customuser=self.request.user)


class PostListView(generics.ListAPIView):
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(customuser_id=self.kwargs.get('pk'))


class CommentsView(CreateUpdateDestroy):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.select_related('user').select_related('post').all()
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {
        'update': [IsAuthor],
        'destroy': [IsAuthor],
    }

    def perform_create(self, serializer):
        serializer.save(customuser=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
