from django.db import models
from django.contrib.auth.models import User

class ChatSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Chat Session {self.session_id}"

class ChatMessage(models.Model):
    SESSION_TYPES = [
        ('user', 'User'),
        ('bot', 'Bot'),
    ]
    
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    message_type = models.CharField(max_length=10, choices=SESSION_TYPES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # Fix the string slicing issue by converting to string first
        content_preview = str(self.content)[:50] if self.content else ""
        return f"{self.message_type}: {content_preview}..."
    
    class Meta:
        ordering = ['timestamp']

class Meeting(models.Model):
    PURPOSE_CHOICES = [
        ('Project Discussion', 'Project Discussion'),
        ('Service Inquiry', 'Service Inquiry'),
        ('Freelance Work', 'Freelance Work'),
        ('General Consultation', 'General Consultation'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Meeting with {self.name} on {self.date} at {self.time}"
    
    class Meta:
        ordering = ['date', 'time']