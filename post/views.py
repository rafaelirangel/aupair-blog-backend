from django.shortcuts import render, redirect, get_object_or_404
from post.models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from django.http import HttpResponseNotAllowed
from .models import Post
# Post views

# User only allowed to update, delete or create a post if he is authenticaded 
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def delete_post(request, post_id):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['DELETE'])