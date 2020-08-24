from django.urls import path
from .views import calendar, add_event
urlpatterns = [
    path('calendar/', calendar, name='calendar_main'),
    path('add_event/', add_event, name='calendar_add'),

]