from django.db import models
import os

# Create your models here.
class Post(models.Model):
    post_img = models.ImageField(upload_to='post_images', null=True, blank=True)
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def delete(self, *args, **kwargs):
        # Delete the image file if it exists
        if self.post_img:
            if os.path.isfile(self.post_img.path):
                os.remove(self.post_img.path)
        super().delete(*args, **kwargs)