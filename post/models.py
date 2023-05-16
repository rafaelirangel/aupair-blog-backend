from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_img = models.ImageField(upload_to='post_images', null=True, blank=True)
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # This connects this model with the user If the user is deleted the comment will be deleted as well
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    # def can_edit(self, user):
    #     return user == self.user

    # def can_delete(self, user):
    #     return user == self.user

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    # This connects this model with the user If the user is deleted the comment will be deleted as well
    # username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    comment_date = models.DateTimeField(auto_now=True)
    
class Like(models.Model):
    # This connects this model with the user If the user is deleted the comment will be deleted as well
    # user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)   
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE) 