
from rest_framework import serializers
from blog.models.comment import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'post', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
