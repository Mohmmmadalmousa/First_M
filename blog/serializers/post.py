
from rest_framework import serializers
from ..models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title_id', 'title', 'content', 'author', 'category']
        read_only_fields = ['title_id']
