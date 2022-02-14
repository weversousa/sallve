from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
