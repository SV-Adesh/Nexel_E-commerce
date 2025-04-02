# Testing & Troubleshooting Guide

## Deployment Verification

### 1. Backend Testing

1. **Test API Endpoints**:
   ```bash
   # Using curl
   curl -X GET https://your-backend-name.onrender.com/api/endpoint/
   
   # Or use Postman
   # Create a collection for your API endpoints and test each one
   ```

2. **Admin Panel Access**:
   - Visit https://your-backend-name.onrender.com/admin/
   - Login with your superuser credentials
   - Verify you can access the admin panel

3. **Check Logs on Render**:
   - Go to your Web Service > Logs
   - Look for any errors or warnings

### 2. Frontend Testing

1. **Test Frontend-Backend Communication**:
   - Open browser developer tools (F12)
   - Go to the Network tab
   - Interact with your app and verify API calls succeed
   - Check for CORS errors in the console

2. **Test All Features**:
   - User authentication
   - Data creation/retrieval
   - Form submissions
   - Any other app-specific functionality

### 3. Common Issues & Solutions

#### CORS Issues
If you're seeing CORS errors:
1. Verify your backend CORS settings in Django:
   ```python
   CORS_ALLOWED_ORIGINS = [
       'https://your-frontend-app.vercel.app',
   ]
   CORS_ALLOW_CREDENTIALS = True
   ```
2. Make sure the URL exactly matches your frontend domain
3. Temporary test: Set `CORS_ALLOW_ALL_ORIGINS = True` (not for production)

#### Database Connection Issues
1. Check DATABASE_URL environment variable in Render
2. Verify migrations were applied:
   ```bash
   # In Render shell
   python manage.py showmigrations
   ```
3. Test database connection:
   ```bash
   # In Render shell
   python manage.py shell
   >>> from django.db import connections
   >>> connections['default'].ensure_connection()
   ```

#### Static Files Not Loading
1. Verify STATIC_ROOT and STATIC_URL settings
2. Make sure WhiteNoise is properly configured
3. Run `python manage.py collectstatic` again via Render shell

#### Frontend API Calls Failing
1. Verify API URL environment variable is correct
2. Check for trailing slashes in API endpoints
3. Inspect network calls in browser dev tools
4. Test API endpoints directly with Postman or curl

## Performance Optimization

1. **Django Performance**:
   - Enable caching
   - Optimize database queries
   - Use Django Debug Toolbar locally to identify bottlenecks

2. **React Performance**:
   - Enable code splitting
   - Implement lazy loading
   - Optimize bundle size with `npm run build -- --profile`

3. **Render Settings**:
   - Consider upgrading to a paid plan for better performance
   - Set appropriate instance type based on traffic

4. **Vercel Settings**:
   - Enable server-side rendering if applicable
   - Configure caching headers 