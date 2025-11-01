from django.contrib import admin
from .models import ProjectCategory, Project, ProjectFile

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_featured', 'order', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('order',)

@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'file_size', 'uploaded_at')
    list_filter = ('project', 'uploaded_at')
    search_fields = ('name', 'project__name')
    ordering = ('-uploaded_at',)