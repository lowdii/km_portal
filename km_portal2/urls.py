"""km_portal2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import dashboard
from machina import urls as machina_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('file_manager/', include('file_manager.urls')),
    path('calendar/', include('calendar_manager.urls')),
    path('forum/', include(machina_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
