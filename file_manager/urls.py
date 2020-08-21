from django.urls import path
from .views import show_categories, show_cat
urlpatterns = [
    path('categories/',show_categories, name='categories'),
    path('categories2/', show_cat , name='categories2'),

]