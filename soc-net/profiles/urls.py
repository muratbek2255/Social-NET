from django.urls import path

from profiles.views import CustomUserView, CustomUserPublicView

urlpatterns = [
    path('profile/<int:pk>/', CustomUserView.as_view({'get': 'retrieve', 'put': 'update'}), name='user-url'),
    path('<int:pk>/', CustomUserPublicView.as_view({'get': 'retrieve'})),
]
