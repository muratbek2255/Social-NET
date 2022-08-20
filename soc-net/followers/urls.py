from django.urls import path

from followers.views import FollowersListView, FollowersView


urlpatterns = [
    path('', FollowersListView.as_view(), name='followers-url'),
    path('<int:pk>/', FollowersView.as_view(), name='add-comments-url')
]