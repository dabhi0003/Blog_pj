from myapp.views import index,post_detail,post_edit,post_delete
from django.contrib import admin
from django.urls import path,include
from user.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/',index,name="index"),
    path("sign-up/",sign_up,name="sign-up"),
    path("",loginview,name="login"),
    path("logout/",logoutview,name="logout"),
    path("profile/",profile,name="profile"),
    path("post-details/<int:id>/",post_detail,name="post_details"),
    path("post-edit/<int:id>/",post_edit,name="post-edit"),
    path("post-delete/<int:id>/",post_delete,name="post-delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
