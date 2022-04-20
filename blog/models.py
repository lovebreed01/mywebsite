from inspect import Attribute
from operator import attrgetter
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

#post category model

class Category(models.Model):
    name = models.CharField( max_length=100)
    class Meta:
        verbose_name_plural = 'Categories'
        
    def get_absolute_url(self):
        return reverse("post", kwargs={
            "pk": self.pk,
            })
    def  __str__(self):
        return self.name

# music artist model
class Artist(models.Model):
    name = models.CharField(max_length=100)
    def  __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    content  = models.TextField()
    file = models.FileField(upload_to='videos')
    posted_on = models.DateTimeField(auto_now=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE )
    def  __str__(self):
        return f'{ self.title } by {self.artist} '

class MusicCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



#music model
class Music(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    music_file = models.FileField(upload_to='songs')
    category = models.ForeignKey(MusicCategory, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE ,)
    image = models.ImageField()
    uploader = models.CharField(max_length=100)
    video_file = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    posted_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()

    def  __str__(self):
        return f'{ self.title } by {self.artist} '

class MusicComment(models.Model):
    author = models.CharField(max_length=100)
    post = models.ForeignKey(Music, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[:2]
#post model
class Post (models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True)
    special = models.BooleanField(default=False)
    trending = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("post", kwargs={
            "slug":self.slug
            })

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()



#comment model
class Comment(models.Model):
    author = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[:2]
