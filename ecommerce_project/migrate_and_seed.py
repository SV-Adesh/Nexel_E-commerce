#!/usr/bin/env python
"""
Script to apply migrations and add sample data if needed.
Run this script on Render shell to ensure database is properly set up.
"""
import os
import django
import sys

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

# Now we can import Django models
from products.models import Product
from django.contrib.auth.models import User
from django.core.management import call_command

def main():
    print("Starting migration and data seeding process...")
    
    # Apply migrations
    print("\n1. Applying migrations...")
    call_command('migrate')
    
    # Check if we have any products
    print("\n2. Checking for existing products...")
    product_count = Product.objects.count()
    print(f"Found {product_count} products in database.")
    
    # If no products, create a sample one
    if product_count == 0:
        print("\n3. No products found. Creating sample product...")
        
        # Create a product
        sample_product = Product(
            name="Sample Product",
            price=100.0,
            description="Test product", 
            inventory=10,
            slug="sample-product"
        )
        
        try:
            sample_product.save()
            print("Sample product created successfully!")
        except Exception as e:
            print(f"Error creating sample product: {str(e)}")
    else:
        print("\n3. Products already exist. No need to create sample.")
    
    # Check for superuser
    print("\n4. Checking for superuser...")
    if not User.objects.filter(is_superuser=True).exists():
        print("No superuser found. Creating superuser...")
        try:
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
            print("Superuser created successfully!")
        except Exception as e:
            print(f"Error creating superuser: {str(e)}")
    else:
        print("Superuser already exists.")
    
    print("\nSetup completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 