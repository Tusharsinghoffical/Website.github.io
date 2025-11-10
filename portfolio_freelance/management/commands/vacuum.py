from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Optimize database performance'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # For SQLite
            if connection.vendor == 'sqlite':
                cursor.execute('PRAGMA optimize')
                cursor.execute('VACUUM')
            # For PostgreSQL
            elif connection.vendor == 'postgresql':
                cursor.execute('VACUUM ANALYZE')
            # For MySQL
            elif connection.vendor == 'mysql':
                cursor.execute('OPTIMIZE TABLE freelancing_service, freelancing_booking, freelancing_payment')
        
        self.stdout.write(
            'Database optimized successfully'
        )