# Deployment Guide for Portfolio Website

This guide will help you deploy your Django portfolio website to various platforms.

## Prerequisites

1. Make sure all changes are committed to your Git repository
2. Ensure you have an account on your chosen deployment platform
3. Install required dependencies: `pip install -r requirements.txt`

## Platform-Specific Deployment Instructions

### Heroku Deployment

1. **Install Heroku CLI**
   - Download and install the Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a new Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set EMAIL_HOST_USER=your-email@gmail.com
   heroku config:set EMAIL_HOST_PASSWORD=your-app-password
   ```

5. **Add PostgreSQL database (optional but recommended)**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

6. **Deploy your app**
   ```bash
   git push heroku main
   ```

7. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   ```

8. **Create superuser (optional)**
   ```bash
   heroku run python manage.py createsuperuser
   ```

9. **Open your app**
   ```bash
   heroku open
   ```

### DigitalOcean Deployment

1. **Create a DigitalOcean account** if you don't have one

2. **Create a new Droplet** with Ubuntu

3. **SSH into your Droplet**
   ```bash
   ssh root@your-droplet-ip
   ```

4. **Update system packages**
   ```bash
   apt update && apt upgrade -y
   ```

5. **Install required software**
   ```bash
   apt install python3 python3-pip nginx postgresql postgresql-contrib -y
   ```

6. **Create a new user for your application**
   ```bash
   adduser portfolio
   usermod -aG sudo portfolio
   ```

7. **Switch to the new user**
   ```bash
   su - portfolio
   ```

8. **Clone your repository**
   ```bash
   git clone your-repository-url
   cd your-repository-folder
   ```

9. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

10. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

11. **Configure PostgreSQL**
    ```bash
    sudo -u postgres psql
    CREATE DATABASE portfolio_db;
    CREATE USER portfolio_user WITH PASSWORD 'secure_password';
    ALTER ROLE portfolio_user SET client_encoding TO 'utf8';
    ALTER ROLE portfolio_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE portfolio_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;
    \q
    ```

12. **Update settings.py** with your database configuration

13. **Run migrations**
    ```bash
    python manage.py migrate
    ```

14. **Collect static files**
    ```bash
    python manage.py collectstatic
    ```

15. **Create superuser**
    ```bash
    python manage.py createsuperuser
    ```

16. **Install and configure Gunicorn**
    ```bash
    pip install gunicorn
    ```

17. **Test Gunicorn**
    ```bash
    gunicorn portfolio_freelance.wsgi:application --bind 0.0.0.0:8000
    ```

18. **Create a Gunicorn systemd service file**
    ```bash
    sudo nano /etc/systemd/system/gunicorn.service
    ```

19. **Configure Nginx** to proxy requests to Gunicorn

20. **Enable and start services**
    ```bash
    sudo systemctl enable gunicorn
    sudo systemctl start gunicorn
    sudo systemctl enable nginx
    sudo systemctl start nginx
    ```

### AWS Deployment (Elastic Beanstalk)

1. **Install Elastic Beanstalk CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize your EB application**
   ```bash
   eb init
   ```

3. **Create and deploy your environment**
   ```bash
   eb create production-env
   ```

4. **Set environment variables**
   ```bash
   eb setenv SECRET_KEY=your-secret-key DEBUG=False
   ```

5. **Deploy updates**
   ```bash
   eb deploy
   ```

6. **Open your application**
   ```bash
   eb open
   ```

## Environment Variables

Make sure to set the following environment variables in production:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to False
- `EMAIL_HOST_USER` - Your email for sending notifications
- `EMAIL_HOST_PASSWORD` - Your email password or app password
- `DATABASE_URL` - Database connection string (if using PostgreSQL)

## Post-Deployment Steps

1. **Verify the deployment** by visiting your website
2. **Test all functionality** including contact forms
3. **Check admin panel** accessibility
4. **Verify email notifications** are working
5. **Monitor logs** for any errors

## Troubleshooting

### Common Issues

1. **Static files not loading**
   - Run `python manage.py collectstatic` 
   - Check STATIC_ROOT and STATIC_URL settings

2. **Database migration errors**
   - Ensure database settings are correct
   - Run `python manage.py migrate` 

3. **Permission denied errors**
   - Check file permissions
   - Ensure proper user ownership

4. **Email not sending**
   - Verify email credentials
   - Check spam folder

### Getting Help

If you encounter issues:
1. Check the logs: `heroku logs --tail` (for Heroku)
2. Verify environment variables are set correctly
3. Ensure all dependencies are installed
4. Check that migrations have been run

For additional support, refer to the Django deployment documentation: https://docs.djangoproject.com/en/5.2/howto/deployment/