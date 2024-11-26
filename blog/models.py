from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
RATINGS= ((0, "Happy Heath"), (1, "Grumpy Croasdale"))

# Create your models here.

class Category(models.Model):
    """ 
    Stores a catogory for each blog post
    """
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


class Post(models.Model):
    """
    Stores a single blog post entry related to :model:'auth.User'.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')   
    category = models.ForeignKey(Category, 
        on_delete=models.PROTECT, default=1, related_name="blog_category") 
    rating = models.IntegerField(choices=RATINGS, default=0)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    social_links = models.URLField(max_length=200, blank=True)
    web_links = models.URLField(max_length=200, blank=True)
    video_links = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Written by {self.author}"    
