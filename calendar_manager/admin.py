from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # list_display = ['title', 'day', 'start_time', 'end_time', 'description']
    pass
