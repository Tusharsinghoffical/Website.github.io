from django.db import models
from django.utils import timezone

class HomePageContent(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Contents"

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class, e.g. 'fas fa-robot'")
    order = models.IntegerField()
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"
        ordering = ['order']