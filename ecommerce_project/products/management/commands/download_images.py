import os
import requests
import time
from django.core.management.base import BaseCommand
from django.conf import settings
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()

class Command(BaseCommand):
    help = 'Download sample product images from Unsplash'

    def process_image(self, image_data, target_size=(800, 600)):
        # Convert bytes to image
        img = Image.open(BytesIO(image_data))
        
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Calculate aspect ratio
        aspect_ratio = target_size[0] / target_size[1]
        
        # Get current dimensions
        width, height = img.size
        
        # Calculate new dimensions maintaining aspect ratio
        if width / height > aspect_ratio:
            # Image is wider than target ratio
            new_width = int(height * aspect_ratio)
            new_height = height
            left = (width - new_width) // 2
            top = 0
            right = left + new_width
            bottom = height
        else:
            # Image is taller than target ratio
            new_width = width
            new_height = int(width / aspect_ratio)
            left = 0
            top = (height - new_height) // 2
            right = width
            bottom = top + new_height
        
        # Crop image to match target aspect ratio
        img = img.crop((left, top, right, bottom))
        
        # Resize to target size
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        
        return img

    def handle(self, *args, **kwargs):
        # Create media/products directory if it doesn't exist
        products_dir = os.path.join(settings.MEDIA_ROOT, 'products')
        os.makedirs(products_dir, exist_ok=True)

        # List of image filenames and direct Unsplash photo IDs
        image_data = [
            ('laptop-gaming.jpg', 'https://images.unsplash.com/photo-1542393545-10f5cde2c810'),
            ('laptop-business.jpg', 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d'),
            ('desktop-pc.jpg', 'https://images.unsplash.com/photo-1593640495253-23196b27a87f'),
            ('mini-pc.jpg', 'https://images.unsplash.com/photo-1593642532842-98d0fd5ebc1a'),
            ('workstation.jpg', 'https://images.unsplash.com/photo-1547586696-ea22b4d4235d'),
            ('chromebook.jpg', 'https://images.unsplash.com/photo-1531297484001-80022131f5a1'),
            ('all-in-one.jpg', 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf'),
            ('student-laptop.jpg', 'https://images.unsplash.com/photo-1498050108023-c5249f4df085'),
            ('creator-laptop.jpg', 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97'),
            ('server-pc.jpg', 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31'),
            ('gaming-mouse.jpg', 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7'),
            ('mechanical-keyboard.jpg', 'https://images.unsplash.com/photo-1587829741301-dc798b83add3'),
            ('gaming-headset.jpg', 'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb'),
            ('gaming-monitor.jpg', 'https://images.unsplash.com/photo-1616763355548-1b606f439f86'),
            ('gaming-chair.jpg', 'https://images.unsplash.com/photo-1598550476439-6847785fcea6'),
            ('mouse-pad.jpg', 'https://images.unsplash.com/photo-1607853202273-797f1c22a38e'),
            ('controller.jpg', 'https://images.unsplash.com/photo-1592840496694-26d035b52b48'),
            ('webcam.jpg', 'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6'),
            ('microphone.jpg', 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc'),
            ('capture-card.jpg', 'https://images.unsplash.com/photo-1561883088-039e53143d73')
        ]

        for filename, image_url in image_data:
            image_path = os.path.join(products_dir, filename)
            
            # Force redownload by removing existing files
            if os.path.exists(image_path):
                os.remove(image_path)
                self.stdout.write(f'Removing existing {filename} for fresh download...')

            try:
                # Add parameters for better quality
                download_url = f'{image_url}?q=85&w=1200&h=800&fit=crop'
                
                # Download the image
                image_response = requests.get(download_url, stream=True)
                image_response.raise_for_status()
                
                # Read the entire image into memory
                image_data = image_response.content
                
                # Process the image
                processed_image = self.process_image(image_data)
                
                # Save the processed image
                processed_image.save(
                    image_path,
                    'JPEG',
                    quality=95,
                    optimize=True
                )
                
                self.stdout.write(self.style.SUCCESS(f'Successfully downloaded and processed {filename}'))
                
                # Add a small delay to avoid rate limiting
                time.sleep(1)
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error processing {filename}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Finished downloading and processing images')) 