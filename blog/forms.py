from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
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
            "featutred_image",
            "location",
            "category",
            "rating",
            "content",
            "excerpt",
            "social_links",
            "web_links",
            "video_links",
        ]

        labels = {
            "title": "Business name",
            "featured_image": "Featured image",
            "location": "Location",
            "category": "Category",
            "rating": "Happy Heath or Grumpy Croasdale",
            "content": "Write your Blog",
            "excerpt": "Your experience in one sentence",
            "social_links": "Facebook page",
            "web_links": "Business Website",
            "video_links": "supporting YouTube channel or video",
        }

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