from rest_framework import serializers

from .models import Post


class PostSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "author_name", "title", "body", "created_at")
        model = Post
