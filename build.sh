#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files with verbosity for debugging
python manage.py collectstatic --no-input --verbosity=2

# Run migrations
python manage.py migrate

# Create cache table for database caching (if needed)
# python manage.py createcachetable