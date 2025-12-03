#!/usr/bin/env python
"""
Deployment script for the portfolio website.
This script automates the deployment process to various platforms.
Version: 2.0.0
"""

import os
import sys
import subprocess
import argparse

def collect_static():
    """Collect static files."""
    print("Collecting static files...")
    try:
        subprocess.run([sys.executable, "manage.py", "collectstatic", "--noinput"], check=True)
        print("Static files collected successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error collecting static files: {e}")
        return False
    return True

def run_migrations():
    """Run database migrations."""
    print("Running database migrations...")
    try:
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
        print("Database migrations completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running migrations: {e}")
        return False
    return True

def create_superuser():
    """Create superuser if it doesn't exist."""
    print("Creating superuser...")
    try:
        # This is a simplified version - in production, you should use environment variables
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Check if superuser exists
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='adminpassword'
            )
            print("Superuser created successfully.")
        else:
            print("Superuser already exists.")
    except Exception as e:
        print(f"Error creating superuser: {e}")
        return False
    return True

def heroku_deploy():
    """Deploy to Heroku."""
    print("Deploying to Heroku...")
    try:
        # Add Heroku remote if not exists
        subprocess.run(["git", "remote", "add", "heroku", "https://git.heroku.com/your-app-name.git"], check=False)
        
        # Deploy
        subprocess.run(["git", "push", "heroku", "main"], check=True)
        print("Deployment to Heroku completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deploying to Heroku: {e}")
        return False
    return True

def prepare_deployment():
    """Prepare the application for deployment."""
    print("Preparing application for deployment...")
    
    # Run collectstatic
    if not collect_static():
        return False
    
    # Run migrations
    if not run_migrations():
        return False
    
    print("Application prepared for deployment successfully.")
    return True

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Deploy portfolio website")
    parser.add_argument(
        "--platform",
        choices=["heroku", "digitalocean", "aws"],
        default="heroku",
        help="Deployment platform"
    )
    
    args = parser.parse_args()
    
    # Prepare deployment
    if not prepare_deployment():
        print("Failed to prepare deployment.")
        return 1
    
    # Deploy based on platform
    if args.platform == "heroku":
        if not heroku_deploy():
            return 1
    else:
        print(f"Deployment to {args.platform} not yet implemented.")
        return 1
    
    print("Deployment completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main())