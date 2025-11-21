from django.db import models
from django.utils import timezone

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image_url = models.URLField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency_level = models.IntegerField(help_text="Proficiency level from 1-100")
    order = models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['order']

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField()
    description = models.TextField(blank=True)
    order = models.IntegerField()
    
    def __str__(self):
        return f"{self.degree} - {str(self.institution)}"
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ['order']

class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    order = models.IntegerField()
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ['order']

class Testimonial(models.Model):
    CLIENT_TYPE_CHOICES = [
        ('indian', 'Indian'),
        ('foreign', 'Foreign'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='testimonials')
    client_name = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100, blank=True)
    client_location = models.CharField(max_length=100)
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPE_CHOICES, default='indian')
    rating = models.IntegerField(help_text="Rating from 1-5")
    testimonial_text = models.TextField()
    project_name = models.CharField(max_length=200, blank=True)
    date = models.DateField()
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.client_name} - {self.project_name}"
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['order', '-date']