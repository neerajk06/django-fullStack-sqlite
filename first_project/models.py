from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# inherit models from Model class

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # string representation of models
    def __str__(self):
        return self.user.username


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    # string representation of models
    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, )
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE, )
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class User(models.Model):
    firstname = models.CharField(max_length=264)
    lastname = models.CharField(max_length=264)
    email = models.CharField(max_length=264)
