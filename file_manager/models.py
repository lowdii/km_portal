from django.db import models

# Create your models here.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import datetime

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Year(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(2010, datetime.date.today().year + 2)]

    year = models.IntegerField( choices=YEAR_CHOICES, default=datetime.datetime.now().year, unique=True)

    def __str__(self):
        return str(self.year)

class SecratariatLevel(models.Model):
    level = models.CharField(max_length=40, unique=True)
    def __str__(self):
        return str(self.level)

class DocumentType(models.Model):
    type = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return str(self.type)