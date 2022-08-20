from django.core.management.base import BaseCommand

from followers.models import Follower
from walls.models import Post
from profiles.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_user()
        self.create_follower()
        self.create_post()
        self.stdout.write('Success')

    def create_user(self):
        for i in range(10):
            user = CustomUser.objects.create(username=f"test {i+2}", email=f"test{i}@gmail.com",
                                      is_active=True, middle_name=f"test {i}",
                                      number_phone=f"0707058388{i}", gender=1)
            user.set_password('messiaguero89')
            user.save()

    def create_follower(self):
        user_all = CustomUser.objects.order_by()[2:]
        for i in user_all:
            follower = Follower.objects.create(user_id=i, subscriber_id=1)

    def create_post(self):
        user_all = CustomUser.objects.all()
        for user in user_all:
            for i in range(10):
                post = Post.objects.create(text=f'Text post', user=user)
