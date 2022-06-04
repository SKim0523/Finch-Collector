from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Finch(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    # rare = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
                
class Comment(models.Model):
    content = models.TextField(max_length=500)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
class List(models.Model):

    name = models.CharField(max_length=150)
    finches = models.ManyToManyField(Finch)

    def __str__(self):
        return self.name