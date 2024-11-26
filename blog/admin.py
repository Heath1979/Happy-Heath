from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Location, Comment

# Register your models here.
admin.site.register(Post)

admin.site.register(Category)

admin.site.register(Location)

admin.site.register(Comment)