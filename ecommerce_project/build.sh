#!/bin/bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run our custom migration and seeding script
python migrate_and_seed.py

# Collect static files
python manage.py collectstatic --no-input 