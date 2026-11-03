
from rest_framework import viewsets, permissions, mixins
from ..models import Comment
from ..serializers import CommentSerializer

class CommentViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
