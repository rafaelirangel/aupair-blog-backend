from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    post_img = models.ImageField(upload_to='post_img', null=True, blank=True)
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def can_edit(self, user):
        return user == self.user
    def delete(self, *args, **kwargs):
        # Delete the image file if it exists
        if self.post_img:
            if os.path.isfile(self.post_img.path):
                os.remove(self.post_img.path)
    def can_delete(self, user):
        return user == self.user
    super().delete(*args, **kwargs)