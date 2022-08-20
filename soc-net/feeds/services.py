from django.conf import settings

from walls.models import Post


class Feed:

    def get_list_post(self, user: settings.AUTH_USER_MODEL):
        return Post.objects.filter(user__owner__subsribers=user).\
            order_by('-created_at').\
            select_related('customuser').\
            prefetch_related('comments')


feed_service = Feed()
