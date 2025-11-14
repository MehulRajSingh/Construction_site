# services/management/commands/create_sample_services.py
from django.core.management.base import BaseCommand
from services.models import Service

class Command(BaseCommand):
    help = 'Create sample services'
    
    def handle(self, *args, **options):
        services_data = [
            {
                'title': 'Residential Construction',
                'short_description': 'Complete home construction services from foundation to finishing touches.',
                'description': 'Professional residential construction services with attention to detail and quality craftsmanship...',
                'category': 'construction',
                'base_price': 50000,
                'duration': '3-6 months',
                'warranty': '90 years',
                'team_size': '20-25 experts',
                'rating': 4.9,
                'badge': 'Popular',
                'features': ['Custom Design', 'Quality Materials', 'Timely Completion', '90-Year Warranty']
            },
            # Add more services...
        ]
        
        for data in services_data:
            Service.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
        
        self.stdout.write(self.style.SUCCESS('Sample services created!'))