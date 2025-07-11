from django.contrib import admin
from .models import Account,UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
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
    
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail','user','city','state','country')

admin.site.register(UserProfile,UserProfileAdmin)