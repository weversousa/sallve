from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model
from pages.models import Page


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = RichTextField()
    video = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title
