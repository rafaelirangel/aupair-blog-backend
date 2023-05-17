from rest_framework import routers
from django.urls import path
from . import views
from .views import (
    PostList,
    PostDetail,
    CommentList,
    CommentDetail,
    LikeList )

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_details'),
    path('posts/<int:pk>/comments/',
         views.CommentList.as_view(), name='comment_list'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/',
         views.CommentDetail.as_view(), name='comment_details'),
    path('posts/likes/<int:pk>', views.LikeList.as_view(), name='like_post'),
]
