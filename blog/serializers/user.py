
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)