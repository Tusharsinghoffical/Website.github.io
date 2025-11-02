from django.shortcuts import render
from .models import HomePageContent, Feature
from typing import Any

def index(request) -> Any:
    # Get content from database
    content = HomePageContent.objects.first()  # type: ignore
    if not content:
        # Create default content if none exists
        content = HomePageContent.objects.create(  # type: ignore
            title='Portfolio & Freelancing Platform',
            subtitle='Showcasing my work and offering freelance services as a Data Scientist and AI Agents Developer',
            description='A passionate Data Scientist and AI Agents Developer with expertise in Python, Machine Learning, and building intelligent AI Agents. I transform complex data into actionable insights and create smart solutions that make a difference.'
        )
    
    # Get features from database
    features = Feature.objects.all()  # type: ignore
    
    # If no features exist, create default ones
    if not features.exists():
        features_data = [
            {
                'title': 'AI Expertise',
                'description': 'Specialized in AI Agents Development and Machine Learning',
                'icon_class': 'fas fa-brain',
                'order': 1
            },
            {
                'title': 'Full Stack',
                'description': 'End-to-end development from concept to deployment',
                'icon_class': 'fas fa-code',
                'order': 2
            },
            {
                'title': 'Fast Delivery',
                'description': 'Efficient project completion with regular updates',
                'icon_class': 'fas fa-bolt',
                'order': 3
            },
            {
                'title': '24/7 Support',
                'description': 'Ongoing support and maintenance for all projects',
                'icon_class': 'fas fa-headset',
                'order': 4
            }
        ]
        
        for feature_data in features_data:
            Feature.objects.create(**feature_data)  # type: ignore
        
        features = Feature.objects.all()  # type: ignore
    
    context = {
        'content': content,
        'features': features,
    }
    
    return render(request, 'home/index.html', context)

def dashboard(request) -> Any:
    # For now, we'll create a simple dashboard
    # In a real application, this would fetch user-specific data
    
    # Sample data for the dashboard
    recent_projects = [
        {
            'title': 'AI Chatbot Solution',
            'status': 'Completed',
            'date': '2025-10-15',
            'description': 'Implemented an intelligent chatbot for customer support'
        },
        {
            'title': 'Data Analysis Dashboard',
            'status': 'In Progress',
            'date': '2025-11-01',
            'description': 'Building a real-time analytics dashboard'
        }
    ]
    
    recent_services = [
        {
            'title': 'Machine Learning Model',
            'date': '2025-10-20',
            'status': 'Delivered'
        },
        {
            'title': 'Web Development',
            'date': '2025-11-05',
            'status': 'Ongoing'
        }
    ]
    
    context = {
        'recent_projects': recent_projects,
        'recent_services': recent_services,
        'user_name': 'Returning Visitor'
    }
    
    return render(request, 'home/dashboard.html', context)