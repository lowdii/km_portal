from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import (
    AbstractUser,
    UserManager as BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        user = super.create_user(
            username=email,
            email=email,
            password=password,
            is_staff=False,
            is_superuser=False,
            first_name=first_name,
            last_name=last_name,
        )
        return user

    def create_superuser(self, email=None, first_name=None, last_name=None, password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        return user

class Division(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Division, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Unit, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class MyUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(('email address'), unique=True)  # changes email to unique and blank to false
    REQUIRED_FIELDS = [('first_name', 'last_name',)]  # removes email from REQUIRED_FIELDS
    objects = UserManager()
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True, blank=True)
    should_change_password = models.BooleanField(null=False, default=True)



