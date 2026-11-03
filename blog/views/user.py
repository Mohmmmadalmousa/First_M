
from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import User
from blog.serializers import UserSerializer

class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


    @api_view(['GET'])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)