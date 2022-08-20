from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets, response

from walls.models import Post
from walls.serializers import ListPostSerializer
from viewsets.classes import MixedPermission

from feeds.services import feed_service


User = get_user_model()


class FeedView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPostSerializer

    def list(self, request, *args, **kwargs):
        posts = feed_service.get_list_post(request.user)
        serializer = self.get_serializer(posts, many=True)
        return response.Response(serializer.data)