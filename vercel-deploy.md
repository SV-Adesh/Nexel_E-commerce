# Vercel Deployment Instructions

1. Connect your GitHub repository to Vercel:
   - Go to https://vercel.com/
   - Sign up/Login with GitHub
   - Click "Add New" > "Project"
   - Select your repository
   - Configure project settings:
     - Framework Preset: Create React App
     - Build Command: `npm run build`
     - Output Directory: `build`
     - Root Directory: `./` (or your frontend directory if monorepo)

2. Environment Variables:
   - Add these in Vercel project settings > Environment Variables:
     - REACT_APP_API_URL=https://your-backend-name.onrender.com/api
     - REACT_APP_ENV=production

3. Deploy Settings:
   - Enable auto-deployments on push
   - Select branch to deploy from (main/master)

4. Custom Domain (Optional):
   - Go to Project Settings > Domains
   - Add your custom domain
   - Follow Vercel's DNS configuration steps

5. After deployment, your app will be available at https://your-project-name.vercel.app 