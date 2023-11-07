from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author','content']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Post
        fields = ['id', 'author','title','text','created_date','image_url','comments']