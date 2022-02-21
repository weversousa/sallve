from django.contrib import admin
from .models import Post, Gallery


# Register your models here.
class GalleryAdmin(admin.StackedInline):
    model=Gallery


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [GalleryAdmin]

    class Meta:
        model=Post
