from django.shortcuts import render
from .models import Service, ServiceCategory, ServiceFeature

def index(request):
    # Get services from database
    services = Service.objects.all()  # type: ignore
    
    # If no services exist, create default ones
    if not services.exists():
        # First, ensure we have service categories
        categories_data = [
            {'name': 'Medical', 'description': 'Medical services', 'icon_class': 'fas fa-laptop-medical', 'order': 1},
            {'name': 'Food', 'description': 'Food services', 'icon_class': 'fas fa-utensils', 'order': 2},
            {'name': 'Marketing', 'description': 'Marketing services', 'icon_class': 'fas fa-bullhorn', 'order': 3},
            {'name': 'AI', 'description': 'AI services', 'icon_class': 'fas fa-robot', 'order': 4},
            {'name': 'Data', 'description': 'Data services', 'icon_class': 'fas fa-chart-bar', 'order': 5},
            {'name': 'Cloud', 'description': 'Cloud services', 'icon_class': 'fas fa-cloud', 'order': 6},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = ServiceCategory.objects.get_or_create(  # type: ignore
                name=cat_data['name'],
                defaults=cat_data
            )
            categories[cat_data['name'].lower()] = category
        
        services_data = [
            {
                'name': 'Medical Website Development',
                'description': 'Creating secure and compliant healthcare websites with patient portals and telemedicine features.',
                'category': categories['medical'],
                'icon_class': 'fas fa-laptop-medical',
                'is_active': True,
                'order': 1
            },
            {
                'name': 'Food Delivery Platform',
                'description': 'Building end-to-end food delivery solutions with real-time tracking and payment integration.',
                'category': categories['food'],
                'icon_class': 'fas fa-utensils',
                'is_active': True,
                'order': 2
            },
            {
                'name': 'Digital Marketing Solutions',
                'description': 'Comprehensive digital marketing services to grow your online presence and customer base.',
                'category': categories['marketing'],
                'icon_class': 'fas fa-bullhorn',
                'is_active': True,
                'order': 3
            },
            {
                'name': 'AI Agents Development',
                'description': 'Developing intelligent AI agents and automation solutions for various business needs.',
                'category': categories['ai'],
                'icon_class': 'fas fa-robot',
                'is_active': True,
                'order': 4
            },
            {
                'name': 'Data Science & Analytics',
                'description': 'Transforming data into actionable insights and building predictive models.',
                'category': categories['data'],
                'icon_class': 'fas fa-chart-bar',
                'is_active': True,
                'order': 5
            },
            {
                'name': 'Cloud Solutions',
                'description': 'Scalable cloud infrastructure and deployment solutions for your applications.',
                'category': categories['cloud'],
                'icon_class': 'fas fa-cloud',
                'is_active': True,
                'order': 6
            }
        ]
        
        for service_data in services_data:
            Service.objects.create(**service_data)  # type: ignore
        
        services = Service.objects.all()  # type: ignore
    
    # Add features to each service (without direct assignment)
    services_with_features = []
    for service in services:
        # Create a copy of the service with features attached
        service_dict = {
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'category': service.category.name.lower() if service.category else 'other',
            'icon_class': service.icon_class,
            'is_active': service.is_active,
            'order': service.order,
            'created_at': service.created_at,
            'updated_at': service.updated_at,
            'features': ServiceFeature.objects.filter(service=service)  # type: ignore
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