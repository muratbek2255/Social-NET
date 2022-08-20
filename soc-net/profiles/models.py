from django.contrib.auth.models import AbstractUser
from django.db import models


class AbstractTimeStampModel(models.Model):

    first_login = models.DateTimeField(auto_now_add=True)
    updated_login = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Gender(models.Model):
    gender = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.gender


class CustomUser(AbstractUser, AbstractTimeStampModel):
    """Кастомный пользователь"""
    middle_name = models.CharField(max_length=50)
    number_phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(default='Im cool')
    github = models.URLField(max_length=200, blank=True, null=True)
    date_birthday = models.DateField(null=True, blank=True)
    gender = models.ForeignKey(to=Gender, on_delete=models.SET_NULL, null=True, blank=True, related_name='genders')
    technology = models.ManyToManyField('Technology', related_name='users')


class Technology(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
