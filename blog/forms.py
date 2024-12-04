from django import forms
from django_summernote.widgets import SummernoteWidget
from django.utils.text import slugify
from .models import Comment, Post


class PostForm(forms.ModelForm):
    """ 
    Allows users to input a new location if current location not available
    """
    location = forms.CharField(max_length=50, label="Location")

    """ 
    Post class for users to create a post
    """
    class Meta:
        """ 
        Specify the model and order of the fields
        """
        model = Post
        fields = [
            "title",
            "featured_image",
            "category",
            "rating",
            "content",
            "excerpt",
            "social_links",
            "web_links",
            "video_links",
        ]

        widgets = {
            'content': SummernoteWidget(),
        }

        labels = {
            "title": "Business name.",
            "featured_image": "Featured image.",
            "category": "Category.",
            "rating": "Happy Heath or Grumpy Croasdale?",
            "content": "Write your Blog.",
            "excerpt": "Your experience in one sentence.",
            "social_links": "Facebook page",
            "web_links": "Business Website",
            "video_links": "Supporting YouTube channel or video.",
        }

    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance    


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """
    class Meta:
        """
        Specify the Django model and order of the fields
        """
        model = Comment
        fields = ('body',)