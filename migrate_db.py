#!/usr/bin/env python
"""
Database migration utility for Django deployment.
Run this script to prepare and migrate your database for production.
"""
import os
import sys
import subprocess
import django
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def run_command(command):
    """Run a shell command and print output."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"Error: {result.stderr}")
        return False
    print(result.stdout)
    return True

def main():
    """Main function to run migrations."""
    print("Django Database Migration Utility")
    print("=================================")
    
    # Check if Django settings module is set
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
        print(f"Setting DJANGO_SETTINGS_MODULE to {os.environ.get('DJANGO_SETTINGS_MODULE')}")
    
    # Check database connection
    print("\nChecking database connection...")
    try:
        django.setup()
        from django.db import connections
        connections['default'].ensure_connection()
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")
        print("Please check your DATABASE_URL environment variable.")
        return False
    
    # Make migrations
    print("\nMaking migrations...")
    if not run_command("python manage.py makemigrations"):
        return False
    
    # Show migrations
    print("\nDisplaying pending migrations...")
    if not run_command("python manage.py showmigrations"):
        return False
    
    # Apply migrations
    print("\nApplying migrations...")
    if not run_command("python manage.py migrate"):
        return False
    
    # Collect static files
    print("\nCollecting static files...")
    if not run_command("python manage.py collectstatic --noinput"):
        return False
    
    print("\nMigration process completed successfully!")
    print("Your database is now ready for production.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 