from django.contrib import admin
from .models import Profile, SkillCategory, Skill, Education, Certification, Testimonial

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'created_at')
    search_fields = ('name', 'title', 'email')
    list_filter = ('created_at',)

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'proficiency_level', 'order')
    list_filter = ('category', 'order')
    search_fields = ('name',)
    ordering = ('order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'degree', 'institution', 'start_date', 'end_date', 'order')
    list_filter = ('profile', 'start_date', 'end_date', 'order')
    search_fields = ('degree', 'institution', 'specialization')
    ordering = ('order',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'name', 'issuing_organization', 'issue_date', 'order')
    list_filter = ('profile', 'issue_date', 'order')
    search_fields = ('name', 'issuing_organization', 'credential_id')
    ordering = ('order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'client_location', 'client_type', 'rating', 'project_name', 'date', 'is_featured')
    list_filter = ('client_type', 'rating', 'is_featured', 'date')
    search_fields = ('client_name', 'client_company', 'project_name', 'testimonial_text')
    ordering = ('order', '-date')