
from rest_framework import viewsets, permissions, mixins
from blog.models import Category
from blog.serializers.category import CategorySerializer

class CategoryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
