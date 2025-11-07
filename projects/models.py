from django.db import models

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, default='fas fa-folder')
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "Project Categories"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1, blank=True, null=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['order', '-date_created']