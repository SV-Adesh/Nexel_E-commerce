import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration using dj-database-url
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

INSTALLED_APPS = [
    # ... existing apps ...
    'corsheaders',
    'core',  # Add your main app
    'src.api',  # Add the API app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add this near the top
    # ... other middleware ...
]

# CORS configuration for production
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')
# For development only - remove in production
# CORS_ALLOW_ALL_ORIGINS = True 