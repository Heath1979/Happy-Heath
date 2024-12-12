from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
RATINGS = ((0, "Happy Heath"), (1, "Grumpy Croasdale"))

# Create your models here.


class Category(models.Model):
    """
    Stores a catogory for each blog post
    """

    type = models.CharField(max_length=50)
    """
    Meta class to show correct plural name
    """

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["type"]

    def __str__(self):
        return self.type


class Location(models.Model):
    """
    Stores a location for each blog post
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Stores a single blog post entry related to :model:'auth.User'.
    category related to :model:'category.Category'.
    location related to :model:'location.Location'.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        default=1,
        related_name="blog_location"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        default=1,
        related_name="blog_category"
    )
    rating = models.IntegerField(choices=RATINGS, default=0)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    social_links = models.URLField(
        max_length=200, blank=False, default='https://example.com')
    web_links = models.URLField(
        max_length=200, blank=False, default='https://example.com')
    video_links = models.URLField(
        max_length=200, blank=False, default='https://example.com')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Written by {self.author}"


class Comment(models.Model):
    """
    stores a single comment entry related to :model: 'auth.User'
    and :model: 'blog.Post'.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
