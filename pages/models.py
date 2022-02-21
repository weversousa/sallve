from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(blank=True, upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
