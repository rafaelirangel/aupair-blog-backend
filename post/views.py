from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from post.models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from django.http import HttpResponseNotAllowed
from .models import Post
# Post views

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]   

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

    # def get_permissions(self):
    #     if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)