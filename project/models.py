from django.db import models
from django.urls import reverse
from users.models import User

# from django.forms import ModelChoiceField

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="project/post_thumbnail/")
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.title
    
    
    
    def get_absolute_url(self):
        return reverse("project:posts", kwargs={"pk": self.pk})
        

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
