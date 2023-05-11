from django.contrib import admin
from .models import PostModel,Comment


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["date_created", "author", "content", "title",'id'][::-1]



@admin.register(Comment)
class Comments(admin.ModelAdmin):
    list_display = ['id',"user", "post", "content"]