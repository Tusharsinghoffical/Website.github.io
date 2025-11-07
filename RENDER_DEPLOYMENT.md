# Render Deployment Guide

This guide will help you deploy your Django portfolio website to Render.

## Prerequisites

1. Create a Render account at https://render.com
2. Connect your GitHub account to Render
3. Fork this repository to your GitHub account (if not already done)

## Deployment Steps

### 1. Create a New Web Service on Render

1. Go to your Render Dashboard
2. Click "New" and select "Web Service"
3. Connect your GitHub repository
4. Give your app a unique name (e.g., `portfolio-website-yourname`)
5. Select the branch to deploy (usually `main` or `master`)

### 2. Configure the Web Service

Render will automatically detect this is a Python application. Confirm the following settings:

- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn portfolio_freelance.wsgi:application`
- **Environment**: Python

### 3. Add Environment Variables

In the "Advanced" section, add the following environment variables:

| Key | Value | Sync |
|-----|-------|------|
| SECRET_KEY | [Generate a new Django secret key] | No |
| DEBUG | False | Yes |
| EMAIL_HOST_USER | your-email@gmail.com | No |
| EMAIL_HOST_PASSWORD | your-app-password | No |
| GEMINI_API_KEY | your-gemini-api-key | No |

### 4. Create a PostgreSQL Database

1. In your Render Dashboard, click "New" and select "PostgreSQL"
2. Give your database a name (e.g., `portfolio-db`)
3. Select the free tier if this is for personal use
4. Note the database credentials for the next step

### 5. Update Database Environment Variables

After creating your database, go back to your web service settings and add:

| Key | Value | Sync |
|-----|-------|------|
| DATABASE_URL | [Copy from your PostgreSQL database credentials] | Yes |

### 6. Deploy

1. Click "Create Web Service"
2. Render will automatically start building and deploying your application
3. The build process will:
   - Install dependencies from `requirements.txt`
   - Run `collectstatic` to gather static files
   - Run migrations to set up the database

### 7. Post-Deployment Configuration

After deployment is complete:

1. **Create a superuser** by running a one-off command in Render:
   - Go to your web service dashboard
   - Click "Connect" to open a shell
   - Run: `python manage.py createsuperuser`

2. **Verify the deployment** by visiting your application URL

## Troubleshooting

### Common Issues

1. **Build failures**:
   - Check that all dependencies in `requirements.txt` are correct
   - Ensure `build.sh` has execute permissions

2. **Database connection errors**:
   - Verify `DATABASE_URL` environment variable is correctly set
   - Check that the PostgreSQL database is provisioned

3. **Static files not loading**:
   - Ensure `STATIC_ROOT` is set in settings
   - Verify `collectstatic` runs during build

4. **Application errors**:
   - Check logs in the Render dashboard
   - Verify all environment variables are set

### Checking Logs

You can monitor your application logs in real-time:
1. Go to your web service dashboard
2. Click "Logs" to view real-time application logs

## Environment Variables Reference

Make sure to set all these environment variables in your Render dashboard:

- `SECRET_KEY` - Django secret key (generate a new one)
- `DEBUG` - Should be `False` in production
- `DATABASE_URL` - Provided by Render PostgreSQL service
- `EMAIL_HOST_USER` - Your email for sending notifications
- `EMAIL_HOST_PASSWORD` - Your email app password
- `GEMINI_API_KEY` - Your Gemini API key for AI features

## Custom Domain (Optional)

To use a custom domain:

1. In your web service dashboard, go to "Settings"
2. Scroll to "Custom Domains"
3. Add your domain name
4. Follow Render's instructions to configure DNS

## Scaling

Render automatically scales your application based on traffic. For more control:

1. Go to your web service dashboard
2. Click "Settings"
3. Modify "Instance Count" and "Instance Size" as needed

Your Django portfolio website is now ready to be deployed on Render!