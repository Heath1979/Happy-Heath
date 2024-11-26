from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category

# Register your models here.
admin.site.register(Post)

admin.site.register(Category)