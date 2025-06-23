from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_join', 'is_active')
    readonly_fields = ('last_login', 'date_join')
    list_display_links = ('email', 'first_name', 'last_name')
    ordering = ('-date_join',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)