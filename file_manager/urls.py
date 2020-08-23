from django.urls import path
from .views import add_document, document_list, download, document_main_page
urlpatterns = [
    path('', document_main_page, name='document_main_page'),
    path('add_document/', add_document, name='add_document'),
    path('list_document/', document_list, name='list_document'),
    path('download/<int:file_id>', download, name='download'),
]