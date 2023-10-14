from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Post
        fields = ['id', 'author','title','text','created_date','image_url']