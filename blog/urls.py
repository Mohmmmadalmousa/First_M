from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import PostViewSet, get_posts
from .views.category import CategoryViewSet
from .views.user import UserViewSet
from .views.comment import CommentViewSet
router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('categories', CategoryViewSet, basename='category')
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')
urlpatterns = [
    path('posts/get_post/', get_posts, name='get_post'),
]
urlpatterns +=router.urls