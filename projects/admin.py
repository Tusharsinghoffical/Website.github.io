from django.contrib import admin
from .models import Project, ProjectCategory

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_created', 'order')
    list_filter = ('category', 'date_created')
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('order',)
    ordering = ('order', '-date_created')
    fields = ('title', 'description', 'category', 'technologies', 'image', 'image_url', 'github_url', 'live_url', 'order')