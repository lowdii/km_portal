from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser, Division, Position, Unit
from .forms import UserCreateForm

class UserAdmin(BaseUserAdmin):
    add_form = UserCreateForm
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Employee details", {
            'fields': ('position', 'division', 'unit'),
        }),
    )
    add_fieldsets = (
        ("Personal info", {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
        ("Employee details", {
            'classes': ('wide',),
            'fields': ( 'position', 'division', 'unit'),
        }),
    )



@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    exclude = ('slug',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    exclude = ('slug',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(MyUser, UserAdmin)

admin.site.site_header = "KM Portal Admin"
admin.site.site_title = "KM Portal Admin"
admin.site.index_title = "Welcome to KM Portal Admin"