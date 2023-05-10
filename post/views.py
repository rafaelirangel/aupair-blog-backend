from django.shortcuts import render

# Create your views here.
from post.models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
# from .models import Post
# Post views


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer
