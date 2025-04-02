# Deployment Checklist

## Pre-Deployment

### Backend (Django)
- [ ] Update all packages in requirements.txt
- [ ] Set DEBUG=False in production settings
- [ ] Set up proper ALLOWED_HOSTS
- [ ] Configure CORS settings for your frontend domain
- [ ] Set up WhiteNoise for static files
- [ ] Create a secure SECRET_KEY for production
- [ ] Set up HTTPS settings (SECURE_SSL_REDIRECT, etc.)
- [ ] Run tests locally to catch issues early
- [ ] Add necessary files (Procfile, render.yaml)

### Frontend (React)
- [ ] Create production environment variables (.env.production)
- [ ] Set correct API URL for the backend
- [ ] Build and test frontend locally
- [ ] Create vercel.json configuration
- [ ] Optimize assets and bundle size

### Database
- [ ] Back up any existing data
- [ ] Prepare migration scripts
- [ ] Test migrations locally

## Deployment Steps

### Database Deployment (Render)
- [ ] Create PostgreSQL database on Render
- [ ] Note connection string for Django

### Backend Deployment (Render)
- [ ] Push code to GitHub
- [ ] Connect repository to Render
- [ ] Configure environment variables
- [ ] Set build and start commands
- [ ] Deploy and check build logs
- [ ] Run migrations via shell if needed
- [ ] Test API endpoints

### Frontend Deployment (Vercel)
- [ ] Push code to GitHub
- [ ] Connect repository to Vercel
- [ ] Configure environment variables
- [ ] Set build settings
- [ ] Deploy and check build logs
- [ ] Set up custom domain (if applicable)

## Post-Deployment

### Testing
- [ ] Test all API endpoints
- [ ] Verify frontend-backend communication
- [ ] Check CORS is working correctly
- [ ] Test all app features
- [ ] Monitor logs for any errors

### Performance
- [ ] Run Lighthouse tests
- [ ] Check load times
- [ ] Optimize any slow queries
- [ ] Implement caching if needed

### Security
- [ ] Verify HTTPS is enabled
- [ ] Check security headers
- [ ] Ensure sensitive data is protected
- [ ] Run security scan (optional)

### Monitoring
- [ ] Set up monitoring tools
- [ ] Configure error notifications
- [ ] Schedule regular backups

## Final Checklist
- [ ] All endpoints work correctly
- [ ] Frontend communicates with backend properly
- [ ] Database migrations are complete
- [ ] Static files are served correctly
- [ ] HTTPS is enabled
- [ ] App performance is satisfactory
- [ ] No errors in logs 