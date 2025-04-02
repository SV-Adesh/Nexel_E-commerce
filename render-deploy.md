# Render Deployment Instructions

## 1. Database Setup

1. Create a PostgreSQL database on Render:
   - Go to https://dashboard.render.com/
   - Sign up/Login
   - Click "New" > "PostgreSQL"
   - Configure database:
     - Name: django-db
     - User: django_user
     - Database: django_db
     - Version: 15 (latest stable)
   - Note your database credentials and connection string

## 2. Backend Deployment

1. Add your Django project to GitHub if not already done

2. Deploy your Django backend:
   - Go to Render dashboard 
   - Click "New" > "Web Service"
   - Connect your GitHub repository
   - Configure service:
     - Name: django-backend
     - Environment: Python
     - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
     - Start Command: `gunicorn your_project.wsgi:application`
     - Specify the Python version: 3.10
   
3. Environment Variables:
   - DJANGO_SECRET_KEY: (generate a secure key)
   - DEBUG: False
   - ALLOWED_HOSTS: .onrender.com
   - DATABASE_URL: (use the Render PostgreSQL connection string)
   - CORS_ALLOWED_ORIGINS: https://your-frontend-app.vercel.app
   - PYTHON_VERSION: 3.10.0

4. Advanced Options:
   - Auto-Deploy: Enable
   - Branch: main/master

## 3. Database Migration

1. Run migrations on Render:
   - Go to your web service
   - Click "Shell"
   - Run: `python manage.py migrate`

## 4. Final Setup

1. Get your backend URL:
   - Your backend will be available at https://your-backend-name.onrender.com

2. Update your frontend environment variables:
   - Go to Vercel project settings
   - Update REACT_APP_API_URL to your Render backend URL

3. Test the connection:
   - Make API requests from frontend to backend
   - Verify CORS is properly configured 