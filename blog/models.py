from django.conf import settings
from django.db import models
from django.utils import timezone
# add a new
from django.contrib.auth.models import AbstractUser, User
from django_extensions.db.fields import AutoSlugField


# create a new model for category 

class Category( models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    
    def __str__(self):
        return self.name
      
# create a new model for a tag
class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    def __str__(self):
        return self.name

# model for post
class Post(models.Model):
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image= models.ImageField(upload_to='post-images/')
    thumbnail_image= models.ImageField(upload_to='post-images/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# add new model to sign-up page
class User(AbstractUser):
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    state = models.CharField(null=True,blank=True)
    city = models.CharField(null=True,blank=True)
    country = models.CharField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.username
    
# create a new model for  comment box 
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.text


