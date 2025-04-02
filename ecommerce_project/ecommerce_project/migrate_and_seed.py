#!/usr/bin/env python
"""
Script to apply migrations and add sample data if needed.
Run this script on Render shell to ensure database is properly set up.
"""
import os
import django
import sys
from io import BytesIO
from django.core.files.base import ContentFile

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

# Now we can import Django models
from products.models import Product, Category
from django.contrib.auth.models import User
from django.core.management import call_command

def generate_placeholder_image():
    """Generate a simple colored rectangle as a placeholder image."""
    try:
        from PIL import Image
        # Create a 600x400 RGB image with a blue background
        img = Image.new('RGB', (600, 400), color=(53, 121, 246))
        img_io = BytesIO()
        img.save(img_io, format='JPEG', quality=90)
        img_io.seek(0)
        return ContentFile(img_io.getvalue(), name="sample-product.jpg")
    except Exception as e:
        print(f"Error creating placeholder image: {str(e)}")
        return None

def main():
    print("Starting migration and data seeding process...")
    
    # Apply migrations
    print("\n1. Applying migrations...")
    call_command('migrate')
    
    # Show migration status
    print("\nShowing migration status:")
    call_command('showmigrations')
    
    # Check if we have any categories
    print("\n2. Checking for existing categories...")
    category_count = Category.objects.count()
    print(f"Found {category_count} categories in database.")
    
    # Create a sample category if none exists
    sample_category = None
    if category_count == 0:
        print("No categories found. Creating sample category...")
        try:
            sample_category = Category(
                name="Sample Category",
                description="A sample category for test products"
            )
            sample_category.save()
            print("Sample category created successfully!")
        except Exception as e:
            print(f"Error creating sample category: {str(e)}")
            return 1
    else:
        # Use the first existing category
        sample_category = Category.objects.first()
    
    # Check if we have any products
    print("\n3. Checking for existing products...")
    product_count = Product.objects.count()
    print(f"Found {product_count} products in database.")
    
    # If no products, create a sample one
    if product_count == 0 and sample_category:
        print("No products found. Creating sample product...")
        
        # Generate a placeholder image
        placeholder_image = generate_placeholder_image()
        
        # Create a product
        try:
            sample_product = Product(
                name="Sample Product",
                price=100.0,
                description="Test product", 
                stock=10,
                slug="sample-product",
                category=sample_category,
                available=True
            )
            
            if placeholder_image:
                sample_product.image = placeholder_image
                
            sample_product.save()
            print("Sample product created successfully!")
        except Exception as e:
            print(f"Error creating sample product: {str(e)}")
            return 1
    else:
        print("Products already exist or no category available. No need to create sample.")
    
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