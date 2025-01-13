import random
import string
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def generate_random_slug(length=8):
    """Generate a random slug consisting of letters and digits."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def create_unique_slug(instance):
    """Generate a unique random slug for the given instance."""
    slug = generate_random_slug()
    # Check for uniqueness
    while instance.__class__.objects.filter(slug=slug).exists():
        slug = generate_random_slug()
    return slug

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Set unique=True
    content = RichTextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  # Add views field
    reading_time = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        word_count = len(self.content.split())
        self.reading_time = max(1, word_count // 200)

        if not self.slug:  # Generate slug if it is not set
            self.slug = create_unique_slug(self)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Research(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Set unique=True
    abstract = models.TextField(default="")
    content_file = models.FileField(upload_to='research/content/', blank=True, null=True)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)  # Add views field
    keywords = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='research/images/', blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug if it is not set
            self.slug = create_unique_slug(self)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='members/')  # Ensure you have Pillow installed
    description = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.name
