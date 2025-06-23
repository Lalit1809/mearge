from django.conf import settings
from django.db import models
from django.utils import timezone
# add a new
from django.contrib.auth.models import AbstractUser, User


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

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