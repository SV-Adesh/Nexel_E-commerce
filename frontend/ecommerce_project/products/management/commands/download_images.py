import os
import requests

# Add this fallback image URL
FALLBACK_IMAGE_URL = 'https://example.com/path/to/default/image.jpg'  # Replace with a valid image URL

# In the loop where you download images
for filename, image_url in image_data:
    image_path = os.path.join(products_dir, filename)

    try:
        # Attempt to download the image
        image_response = requests.get(image_url, stream=True)
        image_response.raise_for_status()
    except Exception as e:
        # If there's an error, use the fallback image
        self.stdout.write(self.style.WARNING(f'Error downloading {filename}: {str(e)}. Using fallback image.'))
        image_response = requests.get(FALLBACK_IMAGE_URL, stream=True)
        image_response.raise_for_status() 