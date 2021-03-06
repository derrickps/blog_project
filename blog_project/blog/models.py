from django.db import models
from django.contrib.auth.models import User # to use foreign key this statement is imported
from django.utils import timezone # to use date time functions this statement is imported
from django.urls import reverse # to use get_absolute_url functionality this statement is imported
from taggit.managers import TaggableManager

# Create your models here.
class CustomManager(models.Manager):  # Custom Manager is used to override inbuilt functionality i.e get_queryset(), objects
    def get_queryset(self):
        return super().get_queryset().filter(status='published') # only published post should come in blog page



class Post(models.Model):
    title = models.CharField(max_length=264)
    slug = models.SlugField(max_length=264,unique_for_date='publish')  # unique_for_date is used to to make each slug unique
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE) # on_delete is important parameter
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects = CustomManager()  # calling our custom Manager
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Commented By {} on {}'.format(self.name,self.post)
