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

    @property
    def get_level(self):
        return self.level

    def __str__(self):
        return str(self.level)

class DocumentType(models.Model):
    type = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return str(self.type)


class ApprovedManager(models.Manager):
    def get_queryset(self):
        return super(ApprovedManager,
                     self).get_queryset()\
                          .filter(approved=True)

class DocumentedInformation(models.Model):

    def upload_folder(self, filename):
        return 'uploads/{}/{}/{}/{}'.format(self.year,self.document_type.type,self.secretariat_level.level, filename)

    YEAR_CHOICES = [(r, r) for r in range(2010, datetime.date.today().year + 2)]

    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    document_type = models.ForeignKey(DocumentType, on_delete=models.DO_NOTHING, null=False, blank=False)
    secretariat_level = models.ForeignKey(SecratariatLevel, on_delete=models.DO_NOTHING, null=False, blank=False)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year, null=False, blank=False)
    file = models.FileField(upload_to=upload_folder, blank=False, null=False)
    created_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    approved_docs = ApprovedManager()

    def __str__(self):
        return self.title



    class Meta:
        ordering = ('-created_date',)