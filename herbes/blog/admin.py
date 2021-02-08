from django.contrib import admin
from .models import Post

# Register your models here.

from .models import Post, PostImage

# @admin.register(PostImage)
class PostImageAdmin(admin.TabularInline): # admin.ModelAdmin
    model = PostImage

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

admin.site.register(Post, PostAdmin)