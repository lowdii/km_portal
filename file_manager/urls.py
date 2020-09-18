from django.urls import path
from .views import add_document, document_list, download, document_main_page, document_list2
urlpatterns = [
    path('', document_main_page, name='document_main'),
    path('add_document/', add_document, name='document_add'),
    path('list_document/<int:type_id>', document_list, name='document_list'),
    path('list_document2/', document_list2, name='document_list2'),
    path('download/<int:file_id>', download, name='document_download'),
]