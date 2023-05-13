from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
