
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Post
from ..serializers import PostSerializer
from ..ai_content.service.summarize import (
    summarize_post,
    PostNotFoundError,
)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def get_posts(request):
    try:
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))

        start = (page - 1) * limit
        end = start + limit

        posts = Post.objects.all()[start:end]
        serializer = PostSerializer(posts, many=True)

        return Response(
            {
                'posts': serializer.data,
                'page': page,
                'limit': limit
            }
        )

    except Exception:
        return Response(
            {"error": "An unexpected error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
def summarize_post_view(request, post_id):
    try:
        result = summarize_post(post_id)

        return Response(
            result,
            status=status.HTTP_200_OK
        )

    except PostNotFoundError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_404_NOT_FOUND
        )

    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST
        )
