#!/usr/bin/env bash
# exit on error
set -o errexit

# Ensure we're using the correct Python version
export PYTHON_VERSION=3.9.16

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations for PostgreSQL
python manage.py migrate

# Create cache table for database caching (if needed)
# python manage.py createcachetable