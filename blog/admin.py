from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Location, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuartion for the Post model.
    """
    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status', 'created_on')


# Register your models here.
admin.site.register(Category)

admin.site.register(Location)

admin.site.register(Comment)
