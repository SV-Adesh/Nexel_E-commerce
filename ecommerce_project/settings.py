DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or whatever database you're using
        'NAME': 'ecommerce_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
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

# For development only
CORS_ALLOW_ALL_ORIGINS = True  # Don't use this in production
# Or specify allowed origins:
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Your frontend URL
] 