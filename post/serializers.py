from rest_framework import serializers
from post.models import Post, Comment, Like

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['comment']

# Like Serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post']

# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'posts', 'comments']


# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'post_img', 'title', 'message',
                  'created_at', 'comments', 'likes_count']

    def get_likes_count(self, post):
        return post.total_likes()
