from django.db import models
from django.utils import timezone

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class, e.g. 'fas fa-robot'")
    order = models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
        ordering = ['order']

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class, e.g. 'fas fa-robot'")
    is_active = models.BooleanField()
    order = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order']

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField()
    
    def __str__(self):
        return f"{self.service.name} - {str(self.title)}"
    
    class Meta:
        verbose_name = "Service Feature"
        verbose_name_plural = "Service Features"
        ordering = ['order']