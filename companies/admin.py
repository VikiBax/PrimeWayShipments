from django.contrib import admin
from .models import Company

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'ein')
    search_fields = ('name', 'ein')
    list_filter = ('active',)
    ordering = ('name','ein')