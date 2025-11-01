from django.shortcuts import render
from .models import Service, ServiceCategory, ServiceFeature

def index(request):
    # Get services from database
    services = Service.objects.all()
    
    # If no services exist, create default ones
    if not services.exists():
        services_data = [
            {
                'name': 'Medical Website Development',
                'description': 'Creating secure and compliant healthcare websites with patient portals and telemedicine features.',
                'category': 'medical',
                'icon_class': 'fas fa-laptop-medical',
                'is_active': True,
                'order': 1
            },
            {
                'name': 'Food Delivery Platform',
                'description': 'Building end-to-end food delivery solutions with real-time tracking and payment integration.',
                'category': 'food',
                'icon_class': 'fas fa-utensils',
                'is_active': True,
                'order': 2
            },
            {
                'name': 'Digital Marketing Solutions',
                'description': 'Comprehensive digital marketing services to grow your online presence and customer base.',
                'category': 'marketing',
                'icon_class': 'fas fa-bullhorn',
                'is_active': True,
                'order': 3
            },
            {
                'name': 'AI Agents Development',
                'description': 'Developing intelligent AI agents and automation solutions for various business needs.',
                'category': 'ai',
                'icon_class': 'fas fa-robot',
                'is_active': True,
                'order': 4
            },
            {
                'name': 'Data Science & Analytics',
                'description': 'Transforming data into actionable insights and building predictive models.',
                'category': 'data',
                'icon_class': 'fas fa-chart-bar',
                'is_active': True,
                'order': 5
            },
            {
                'name': 'Cloud Solutions',
                'description': 'Scalable cloud infrastructure and deployment solutions for your applications.',
                'category': 'cloud',
                'icon_class': 'fas fa-cloud',
                'is_active': True,
                'order': 6
            }
        ]
        
        for service_data in services_data:
            Service.objects.create(**service_data)
        
        services = Service.objects.all()
    
    # Add features to each service (without direct assignment)
    services_with_features = []
    for service in services:
        # Create a copy of the service with features attached
        service_dict = {
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'category': service.category,
            'icon_class': service.icon_class,
            'is_active': service.is_active,
            'order': service.order,
            'created_at': service.created_at,
            'updated_at': service.updated_at,
            'features': ServiceFeature.objects.filter(service=service)
        }
        services_with_features.append(service_dict)
    
    # Group services by category
    categories = {}
    for service_dict in services_with_features:
        category = service_dict['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(service_dict)
    
    context = {
        'services': services_with_features,
        'categories': categories,
    }
    
    return render(request, 'services/index.html', context)