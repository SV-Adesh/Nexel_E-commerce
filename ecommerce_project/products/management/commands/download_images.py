import os
import requests
import random
import urllib3
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files.base import ContentFile
from products.models import Product

# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Command(BaseCommand):
    help = 'Download sample product images from Unsplash'

    def handle(self, *args, **options):
        # Create the media/products directory if it doesn't exist
        products_dir = os.path.join(settings.MEDIA_ROOT, 'products')
        if not os.path.exists(products_dir):
            os.makedirs(products_dir)
        
        # Get all products
        products = Product.objects.all()
        
        # Unsplash API key from environment variable
        unsplash_access_key = os.environ.get('UNSPLASH_ACCESS_KEY')
        
        if not unsplash_access_key:
            self.stdout.write(self.style.ERROR('UNSPLASH_ACCESS_KEY not found in environment variables'))
            return
        
        categories = {
            'Electronics': ['electronics', 'gadgets', 'technology'],
            'Clothing': ['clothing', 'fashion', 'apparel'],
            'Books': ['books', 'reading', 'library'],
            'Home': ['home', 'interior', 'furniture'],
            'Beauty': ['beauty', 'cosmetics', 'skincare'],
            'Sports': ['sports', 'fitness', 'exercise'],
            'Food': ['food', 'groceries', 'cooking'],
            'Office Electronics': ['office', 'business equipment', 'workplace'],
            'Computer Hardware': ['computer', 'hardware', 'pc parts'],
            'Mobile Accessories': ['mobile', 'smartphone', 'accessories'],
            'Gaming': ['gaming', 'video games', 'console'],
            'Headphones': ['headphones', 'audio', 'music'],
        }
        
        for product in products:
            # Get a search term based on the product's category name
            category_name = product.category.name
            search_terms = categories.get(category_name, ['product'])
            search_term = random.choice(search_terms)
            
            # Use product name as additional search term
            query = f"{search_term} {product.name}"
            
            try:
                # Request image from Unsplash
                response = requests.get(
                    'https://api.unsplash.com/photos/random',
                    params={
                        'query': query,
                        'orientation': 'landscape',
                    },
                    headers={
                        'Authorization': f'Client-ID {unsplash_access_key}'
                    },
                    verify=False  # Disable SSL verification for development
                )
                
                if response.status_code == 200:
                    image_data = response.json()
                    image_url = image_data['urls']['regular']
                    
                    # Download the image
                    image_response = requests.get(image_url, verify=False)  # Disable SSL verification
                    if image_response.status_code == 200:
                        # Create a unique filename
                        image_name = f"{product.id}_{product.slug}.jpg"
                        
                        # Save the image
                        product.image.save(
                            image_name,
                            ContentFile(image_response.content),
                            save=True
                        )
                        
                        self.stdout.write(self.style.SUCCESS(f'Image downloaded for {product.name}'))
                    else:
                        self.stdout.write(self.style.ERROR(f'Failed to download image for {product.name}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Unsplash API error: {response.status_code} - {response.text}'))
            
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error downloading image for {product.name}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS('Image download process completed')) 