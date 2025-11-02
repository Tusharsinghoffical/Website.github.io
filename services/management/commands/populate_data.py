from django.core.management.base import BaseCommand
from services.models import ServiceCategory, Service

class Command(BaseCommand):
    help = 'Populate the database with initial service categories and services'

    def handle(self, *args, **options):
        # Create service categories
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
            if created:
                self.stdout.write(f'Created category: {category.name}')
            else:
                self.stdout.write(f'Category already exists: {category.name}')

        # Create services
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
            }
        ]

        for service_data in services_data:
            service, created = Service.objects.get_or_create(  # type: ignore
                name=service_data['name'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'Created service: {service.name}')
            else:
                self.stdout.write(f'Service already exists: {service.name}')

        self.stdout.write(
            'Successfully populated the database with initial data'
        )