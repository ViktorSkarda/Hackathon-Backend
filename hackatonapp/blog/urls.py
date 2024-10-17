from django.urls import path
from .views import CreatePostAPIView

urlpatterns = [
    path('api/posts/', CreatePostAPIView.as_view(), name='create_post_api'),
]
