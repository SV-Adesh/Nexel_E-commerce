#!/bin/bash

# exit on error
set -o errexit

cd ecommerce_project
pip install -r ../requirements.txt

# Apply database migrations
python manage.py migrate

# Run our migration and seeding script for sample data
python ecommerce_project/migrate_and_seed.py

# Collect static files
python manage.py collectstatic --no-input