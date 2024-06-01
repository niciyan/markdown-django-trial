from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'body_html', 'created_at', 'updated_at']
        extra_kwargs = {'body_html': {'read_only': True}}