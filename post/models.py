from django.db import models

# Create your models here.
class Post(models.Model):
    post_img = models.ImageField(upload_to='post_images', null=True, blank=True)
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    

    