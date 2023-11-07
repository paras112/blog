from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

