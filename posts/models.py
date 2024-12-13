from django.db import models

# Create your models here.
from django.db import models
from billapp.models import CustomUser

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
