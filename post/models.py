from django.db import models

# Post model
class Post(models.Model):
    post_img = models.ImageField(upload_to='post_img', null=True, blank=True)
    title = models.CharField(max_length=50, blank=False)
    message = models.CharField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField('Like', related_name='liked_posts')

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

# Comment Model
class Comment(models.Model):
    # This connects this model with the user If the user is deleted the comment will be deleted as well
    # username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250, blank=True)
    comment_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    # If I want to display it by date
    # class Meta:
    #     ordering = ['comment_date']

# Like model
class Like(models.Model):
    # username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)

