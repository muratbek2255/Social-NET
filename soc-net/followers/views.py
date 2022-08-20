from rest_framework import generics, permissions, views, response

from followers.models import Follower
from followers.serializers import FollowersListSerializer
from profiles.models import CustomUser


class FollowersListView(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowersListSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class FollowersView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = CustomUser.objects.filter(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=201)

