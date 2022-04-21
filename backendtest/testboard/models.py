from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    writer = models.ForeignKey(get_user_model(), models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("Post", models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(get_user_model(), models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:30]}..."
