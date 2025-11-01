from django.contrib import admin
from .models import HomePageContent, Feature

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle')
    list_filter = ('created_at', 'updated_at')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    list_filter = ('order',)
    ordering = ('order',)