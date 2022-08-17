from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='published')

# Create your models here.
class Post(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=250)

    # A slug field in Django is used to store and generate valid URLs for
    # your dynamically created web pages.
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    objects = models.Manager() # the default manager
    published = PublishedManager() # our customer manager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='published')
