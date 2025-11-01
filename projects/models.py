from django.db import models
from django.utils import timezone

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class, e.g. 'fas fa-robot'")
    order = models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"
        ordering = ['order']

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20)
    technologies = models.TextField(help_text="Comma-separated list of technologies used")
    image_url = models.URLField(blank=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_featured = models.BooleanField()
    order = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['order']

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=500)
    file_size = models.IntegerField(help_text="File size in bytes")
    download_url = models.URLField()
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.project.name} - {str(self.name)}"
    
    class Meta:
        verbose_name = "Project File"
        verbose_name_plural = "Project Files"
        ordering = ['-uploaded_at']