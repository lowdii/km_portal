from django.shortcuts import render, redirect, reverse
from .forms import DocumentedInformationForm
from .models import DocumentedInformation, DocumentType
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.http import FileResponse
from django.db.models import Q
# Create your views here.


def document_main_page(request):
    form = DocumentedInformationForm
    added_document = bool(request.GET.get('added_document', False))
    doc_types = DocumentType.objects.all()
    return render(request,
                  'document/document.html',
                  {'form': form,
                   'doc_types': doc_types,
                   'added_flag': added_document})


def add_document(request):
    if request.method == 'POST':
        doc_form = DocumentedInformationForm(request.POST, request.FILES)
        if doc_form.is_valid():
            new_doc = doc_form.save(commit=False)
            new_doc.save()
            return redirect('{}?added_document=True'.format(reverse('document_main')))
    else:
        return 'test'


def document_list(request, type_id):
    doc_types = DocumentType.objects.all()
    object_list = DocumentedInformation.approved_docs.filter(document_type=type_id)
    form = DocumentedInformationForm
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
                   'documents': documents,
                   'doc_types': doc_types,
                   'selected_type': type_id,
                   'form':form})


def download(request, file_id):
    doc_info = DocumentedInformation.approved_docs.get(id=file_id)
    filename = doc_info.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


def document_list2(request):
    doc_types = DocumentType.objects.all()
    types = request.GET.getlist('types', None)
    keyword = request.GET.get('keyword', '')
    object_list = DocumentedInformation.approved_docs.get_queryset()

    if keyword != None and keyword !='':
        object_list =  object_list.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))

    if types != None and len(types) > 0:
        object_list =  object_list.filter(Q(document_type__in=types))
    form = DocumentedInformationForm
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
                   'documents': documents,
                   'doc_types': doc_types,
                   'keyword': keyword,
                   'types':  list(map(int, types)),
                   'form':form})