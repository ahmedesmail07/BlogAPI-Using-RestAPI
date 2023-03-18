from django.contrib import admin

from .models import Post


class PostAdminView(admin.ModelAdmin):
    list_display = ["author", "title", "body"]


admin.site.register(Post, PostAdminView)
