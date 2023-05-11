from django.contrib import admin
from .models import ProfileModel

@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ["image", "user"][::-1]
