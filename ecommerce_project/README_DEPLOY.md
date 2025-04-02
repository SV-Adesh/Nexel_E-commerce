# Deployment Instructions for Render

This document provides step-by-step instructions for deploying the Django backend and React frontend on Render.

## Backend Deployment

1. Sign up/login to [Render](https://render.com)
2. Click "New +" button and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: ecommerce-backend (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn ecommerce_project.wsgi:application`
   - **Root Directory**: `ecommerce_project` (if your repository contains both frontend and backend)

5. Under "Advanced" settings, add these environment variables:
   - `DEBUG`: False
   - `SECRET_KEY`: (use a secure, random key)
   - `DATABASE_URL`: (Render will automatically provide this if you use their PostgreSQL service)
   - `STRIPE_SECRET_KEY`: Your Stripe secret key
   - `STRIPE_PUBLISHABLE_KEY`: Your Stripe publishable key
   - `RENDER_EXTERNAL_HOSTNAME`: (This will be automatically set by Render)

6. Select the Free instance type
7. Click "Create Web Service"

## PostgreSQL Database Setup on Render

1. Click "New +" and select "PostgreSQL"
2. Configure your database:
   - **Name**: ecommerce-db (or your preferred name)
   - Select Free tier
3. Create the database
4. The `DATABASE_URL` will be automatically set as an environment variable for your web service if you connect them

## Frontend Deployment

1. Click "New +" button and select "Static Site"
2. Connect your GitHub repository
3. Configure the service:
   - **Name**: ecommerce-frontend (or your preferred name)
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `build`
   - **Root Directory**: `frontend` (point to your frontend directory)

4. Under "Advanced" settings, add these environment variables:
   - `REACT_APP_API_URL`: URL of your backend (e.g., https://ecommerce-backend.onrender.com)
   - `REACT_APP_STRIPE_PUBLISHABLE_KEY`: Your Stripe publishable key

5. Click "Create Static Site"

## Update CORS Settings

After deployment, update the backend's CORS settings to include your frontend URL:

1. Go to your backend web service in Render
2. Update the CORS_ALLOWED_ORIGINS environment variable in settings.py to include:
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://your-frontend-url.onrender.com",
   ]
   ```

## Important Notes

1. Free tier services on Render will spin down after 15 minutes of inactivity. The first request after inactivity will take some time.

2. Make sure to update the API endpoint URLs in your frontend code to point to your deployed backend.

3. Render offers a free tier with some limitations:
   - 750 hours of running time per month
   - Spins down after 15 minutes of inactivity
   - Limited bandwidth and resources

4. To avoid exposing sensitive information, never commit your .env file to your repository.

5. You may need to manually run migrations the first time via the Render shell. 