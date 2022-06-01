from django.db import models

# Create your models here.

class Finch(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    # rare = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
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