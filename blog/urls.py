
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, get_posts, generate_post, summarize_post_view
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
    path('posts/generate/', generate_post, name='generate_post'),
path('posts/<int:post_id>/summarize/',summarize_post_view,name='summarize-post'
),
]

urlpatterns += router.urls
