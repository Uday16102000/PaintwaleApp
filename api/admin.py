from django.contrib import admin
from paintwaleapp.models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'active']
    search_fields = ['username', 'email']
    ordering = ['username']
    
# Register your models here.
admin.site.register(Users, CustomUserAdmin)
admin.site.register(City)