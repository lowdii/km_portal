from django.contrib import admin

# Register your models here.

from mptt.admin import MPTTModelAdmin
from .models import Category
from .models import Year
from .models import SecratariatLevel
from .models import DocumentType

class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    pass

@admin.register(SecratariatLevel)
class SecratariatLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'description',)

