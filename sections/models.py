from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model
from pages.models import Page


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)


class Gallery(models.Model):
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
