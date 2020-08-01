from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
# Create your models here.

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")
class Post(models.Model):
    status_choices=(("draft","Draft"),("published","Published"))
    author=models.ForeignKey(User,related_name="blog_posts")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    body=models.TextField()
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique_for_date="publish")
    status=models.CharField(max_length=10,choices=status_choices,default="draft")
    objects=CustomManager()
    tags=TaggableManager()

    class Meta():
        ordering=("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",args=[self.publish.year,self.publish.strftime("%m"),self.publish.strftime("%d"),self.slug])



class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments")
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=("-created",)

    def __str__(self):
        return "Commented By {} On {}".format(self.name,self.post)


class Feedback(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    feedback=models.TextField()
