from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    all_day = models.BooleanField(default=False)
    start = models.DateTimeField()
    end = models.DateTimeField()

