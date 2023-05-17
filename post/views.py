from rest_framework.views import APIView
from .models import Post, Comment, Like
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.db.models import F

# Post CRUD


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def perform_destroy(self, instance):
        # Delete associated image if any
        if instance.post_img:
            instance.post_img.delete()
        instance.delete()


# Comment CRUD
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


# Likes
class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_id)

        # Check if the post already has a like
        if Like.objects.filter(post=post).exists():
            # Unlike the post
            Like.objects.filter(post=post).delete()

            # Decrement the like count on the post
            Post.objects.filter(pk=post_id).update(
                likes_count=F('likes_count') - 1)

            return Response({'detail': 'Post unliked'}, status=200)
        else:
            # Create a like for the post
            like = Like(post=post)
            like.save()

            # Increment the like count on the post
            Post.objects.filter(pk=post_id).update(
                likes_count=F('likes_count') + 1)

            serializer = self.get_serializer(like)
            return Response(serializer.data, status=201)
