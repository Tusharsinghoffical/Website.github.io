from django.contrib import admin
from .models import ServiceCategory, Service, ServiceFeature

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'order')
    list_filter = ('category', 'is_active', 'order')
    search_fields = ('name', 'description')
    ordering = ('order',)

@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('service', 'title', 'order')
    list_filter = ('service', 'order')
    search_fields = ('title', 'description')
    ordering = ('order',)