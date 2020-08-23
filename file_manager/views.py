from django.shortcuts import render
from .forms import DocumentedInformationForm
from .models import DocumentedInformation
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.http import FileResponse
# Create your views here.


def document_main_page(request):
    return render(request,
                  'document/document.html',
                  {'section': 'dashboard'})


def add_document(request):
    form = DocumentedInformationForm
    return render(request,
                  'document/add_document.html',
                  {'form': form})


def document_list(request):
    object_list = DocumentedInformation.approved_docs.all()

    paginator = Paginator(object_list, 15)
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        documents = paginator.page(paginator.num_pages)
    return render(request,
                  'document/list_document.html',
                  {'page': page,
                   'documents': documents})


def download(request, file_id):
    doc_info = DocumentedInformation.approved_docs.get(id=file_id)
    filename = doc_info.file.path
    response = FileResponse(open(filename, 'rb'))
    return response