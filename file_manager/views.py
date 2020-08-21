from django.shortcuts import render
from .models import Category, Year, SecratariatLevel, DocumentType
# Create your views here.
def show_categories(request):
    return render(request, "categories.html", {'categories': Category.objects.all()})


def show_cat(request):
    return render(request, "categories3.html", {'year': Year.objects.all(), 'level': SecratariatLevel.objects.all(), 'doc_type': DocumentType.objects.all()})