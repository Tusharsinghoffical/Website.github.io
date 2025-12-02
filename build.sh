#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# For MongoDB, we don't need traditional migrations, but we can ensure the database is ready
# python manage.py migrate

# Create cache table for database caching (if needed)
# python manage.py createcachetable