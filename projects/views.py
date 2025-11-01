from django.shortcuts import render
from .models import Project, ProjectCategory, ProjectFile

def index(request):
    # Get projects from database
    projects = Project.objects.all()
    
    # If no projects exist, create default ones
    if not projects.exists():
        projects_data = [
            {
                'name': 'E-commerce Platform',
                'description': 'A full-featured online shopping platform with payment integration and inventory management.',
                'category': 'ecommerce',
                'technologies': 'Django, PostgreSQL, Stripe API',
                'image_url': 'https://via.placeholder.com/400x250',
                'project_url': '#',
                'github_url': '#',
                'is_featured': True,
                'order': 1
            },
            {
                'name': 'Healthcare Management System',
                'description': 'A comprehensive system for managing patient records and appointments with telemedicine features.',
                'category': 'medical',
                'technologies': 'React, Node.js, MongoDB',
                'image_url': 'https://via.placeholder.com/400x250',
                'project_url': '#',
                'github_url': '#',
                'is_featured': True,
                'order': 2
            },
            {
                'name': 'Data Analytics Dashboard',
                'description': 'Interactive dashboard for visualizing business metrics and KPIs with real-time updates.',
                'category': 'data',
                'technologies': 'Python, D3.js, Flask',
                'image_url': 'https://via.placeholder.com/400x250',
                'project_url': '#',
                'github_url': '#',
                'is_featured': False,
                'order': 3
            },
            {
                'name': 'AI Chatbot (SONA)',
                'description': 'Intelligent chatbot for customer support automation with natural language processing capabilities.',
                'category': 'ai',
                'technologies': 'Python, NLP, TensorFlow',
                'image_url': 'https://via.placeholder.com/400x250',
                'project_url': '#',
                'github_url': '#',
                'is_featured': True,
                'order': 4
            }
        ]
        
        for project_data in projects_data:
            Project.objects.create(**project_data)
        
        projects = Project.objects.all()
    
    # Add files to each project (without direct assignment)
    projects_with_files = []
    for project in projects:
        # Create a copy of the project with files attached
        project_dict = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'category': project.category,
            'technologies': project.technologies,
            'image_url': project.image_url,
            'project_url': project.project_url,
            'github_url': project.github_url,
            'is_featured': project.is_featured,
            'order': project.order,
            'created_at': project.created_at,
            'updated_at': project.updated_at,
            'files': ProjectFile.objects.filter(project=project)
        }
        projects_with_files.append(project_dict)
    
    # Define categories
    categories = [
        {
            'name': 'Medical Projects',
            'icon_class': 'fas fa-laptop-medical',
            'description': 'Healthcare applications and systems'
        },
        {
            'name': 'Food Delivery',
            'icon_class': 'fas fa-utensils',
            'description': 'Restaurant and delivery platforms'
        },
        {
            'name': 'AI Projects',
            'icon_class': 'fas fa-robot',
            'description': 'Machine learning and AI applications'
        }
    ]
    
    context = {
        'projects': projects_with_files,
        'categories': categories,
    }
    
    return render(request, 'projects/index.html', context)