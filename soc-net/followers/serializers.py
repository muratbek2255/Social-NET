from rest_framework import serializers

from followers.models import Follower
from profiles.serializers import UserByFollowers


class FollowersListSerializer(serializers.ModelSerializer):
    # subscriber = UserByFollowers(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber', 'user')