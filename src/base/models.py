import cv2
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django_resized import ResizedImageField


class Post(models.Model):
    image = ResizedImageField(size=[300, 300], blank=True, upload_to='posts')
    content = models.TextField(blank=True, max_length=3000)
    title = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    profil_picture = models.ImageField(upload_to='profil_pictures',
                                       default=f'{settings.MEDIA_ROOT}/profil_pictures/profil_picture_default.png',
                                       max_length=300)
    birthdate = models.DateField()
    adress = models.CharField(max_length=255, blank=True, null=True)
    connections = models.ManyToManyField("self", symmetrical=True)
    posts = models.ManyToManyField(Post, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['birthdate']

