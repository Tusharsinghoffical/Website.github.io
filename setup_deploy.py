#!/usr/bin/env python
"""
Setup script for initial deployment configuration.
"""

import os
import sys
import subprocess
import secrets
import string

def generate_secret_key():
    """Generate a new secret key."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(50))

def update_env_file():
    """Update the .env file with a new secret key."""
    env_file = '.env'
    
    if os.path.exists(env_file):
        # Read existing content
        with open(env_file, 'r') as f:
            lines = f.readlines()
        
        # Generate new secret key
        new_secret_key = generate_secret_key()
        
        # Update secret key line
        with open(env_file, 'w') as f:
            for line in lines:
                if line.startswith('SECRET_KEY='):
                    f.write(f'SECRET_KEY={new_secret_key}\n')
                else:
                    f.write(line)
        
        print("Updated .env file with new secret key")
        return True
    else:
        print(".env file not found")
        return False

def collect_static_files():
    """Collect static files."""
    try:
        subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput', '--clear'], check=True)
        print("Static files collected successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error collecting static files: {e}")
        return False

def run_migrations():
    """Run database migrations."""
    try:
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
        print("Database migrations completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running migrations: {e}")
        return False

def create_superuser():
    """Create a superuser."""
    try:
        # Create a simple superuser for initial setup
        from django.core.management import execute_from_command_line
        import django
        from django.conf import settings
        
        # Setup Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_freelance.settings')
        django.setup()
        
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Check if superuser exists
        if not User.objects.filter(is_superuser=True).exists():
            user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin12345'
            )
            print("Superuser 'admin' created with password 'admin12345'")
            print("IMPORTANT: Change this password after first login!")
        else:
            print("Superuser already exists")
        
        return True
    except Exception as e:
        print(f"Error creating superuser: {e}")
        return False

def main():
    """Main setup function."""
    print("Setting up deployment configuration...")
    
    # Update .env file with new secret key
    if not update_env_file():
        print("Warning: Could not update .env file")
    
    # Collect static files
    if not collect_static_files():
        print("Warning: Could not collect static files")
    
    # Run migrations
    if not run_migrations():
        print("Error: Could not run migrations")
        return 1
    
    # Create superuser
    if not create_superuser():
        print("Warning: Could not create superuser")
    
    print("\nDeployment setup completed!")
    print("Next steps:")
    print("1. Review and update the .env file with your actual credentials")
    print("2. Check the DEPLOYMENT_GUIDE.md for platform-specific instructions")
    print("3. Commit your changes to Git")
    print("4. Deploy to your chosen platform")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())