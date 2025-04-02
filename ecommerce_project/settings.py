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
CORS_ALLOWED_ORIGINS = [
    'https://nexelecommerce.vercel.app',
    'https://nexelecommerce-4xad9mouk-adeshs-projects-d64f64b4.vercel.app',
    'https://nexel-ecommerce.vercel.app'
]

# Add additional CORS settings
CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 86400  # 24 hours
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# For development only - remove in production
# CORS_ALLOW_ALL_ORIGINS = True 