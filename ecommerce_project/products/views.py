from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
from .models import Product

def generate_placeholder_image(width=600, height=400, text=None):
    """Generate a placeholder image with optional text."""
    # Create a new image with a random background color
    r = random.randint(100, 200)
    g = random.randint(100, 200)
    b = random.randint(100, 200)
    
    image = Image.new('RGB', (width, height), color=(r, g, b))
    draw = ImageDraw.Draw(image)
    
    # Draw product name if provided
    if text:
        try:
            # Use a default font
            draw.text((width//2, height//2), text, fill=(255, 255, 255), anchor="mm")
        except Exception:
            # If there's an issue with text rendering, just use the colored background
            pass
    
    # Convert to bytes
    img_io = BytesIO()
    image.save(img_io, format='JPEG', quality=90)
    img_io.seek(0)
    
    return img_io.getvalue()

def fix_product_images(request):
    """Fix missing product images by generating placeholders."""
    products = Product.objects.all()
    fixed_count = 0
    
    for product in products:
        if not product.image or not product.image.name:
            # Generate placeholder image
            image_data = generate_placeholder_image(text=product.name)
            
            # Create a filename
            image_name = f"{product.id}_{product.slug}.jpg"
            
            # Save the image
            product.image.save(image_name, ContentFile(image_data), save=True)
            fixed_count += 1
    
    return HttpResponse(f"Fixed {fixed_count} product images with placeholders.")
