# Tushar Singh - Portfolio Website

A professional portfolio website showcasing projects, services, and skills as a Data Scientist and AI Agents Developer.

## 🛠️ Recent Deployment Fixes

1. **Fixed Python version incompatibility (December 2025)**: Resolved `ModuleNotFoundError: No module named 'distutils'` error during deployment. The project now correctly uses Python 3.9.16 which is compatible with Django 3.1.12.

2. **Removed MongoDB and switched to PostgreSQL (December 2025)**: Replaced MongoDB with PostgreSQL for better compatibility and reliability.

## 🌐 Live Demo

- **Development**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Production**: [https://codewithmrsingh.tech](https://codewithmrsingh.tech)

## 📋 Project Overview

This portfolio website highlights the work of Tushar Singh, a seasoned Data Scientist and AI Agents Developer with expertise in Python, Machine Learning, and building intelligent automation systems that drive measurable business results. The site transforms complex data into strategic business insights and creates smart solutions that solve real-world challenges.

## 🛠️ Technologies Used

### Core Technologies
- **Django 4.2** - Web framework
- **Python 3.12.9** - Programming language
- **HTML5/CSS3** - Markup and styling
- **JavaScript (ES6+)** - Client-side scripting
- **Bootstrap 5** - CSS framework
- **SQLite** - Development database
- **PostgreSQL** - Production database

### Libraries & Tools
- **Gunicorn** - Production WSGI server
- **Whitenoise** - Static file serving
- **django-extensions** - Development utilities
- **Pillow** - Image processing
- **Requests** - HTTP library
- **OpenAI** - AI integration
- **Font Awesome** - Icon library

## 📁 Project Structure

```
Portfolio/
├── about/                 # About page with professional profile
├── chat/                  # Chat functionality with AI integration
├── contact/               # Contact form with email notifications
├── freelancing/           # Freelance services and booking system
├── home/                  # Homepage and main navigation
├── projects/              # Project showcase and portfolio
├── services/              # Service offerings and details
├── portfolio_freelance/   # Main Django project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── statics/               # Static assets (images, CSS, JS)
├── templates/             # HTML templates
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku deployment configuration
├── render.yaml            # Render deployment configuration
├── build.sh               # Build script for deployment
├── runtime.txt            # Python runtime version
├── deploy.py              # Deployment automation script
└── manage.py              # Django management script
```

## ✨ Key Features

### Professional Portfolio
- **Responsive Design**: Mobile-first approach with full responsiveness
- **Modern UI**: Clean design with vibrant gradients and smooth animations
- **SEO Optimized**: Meta tags, structured data, and sitemap for better search rankings
- **Performance Focused**: Caching, compression, and optimized asset delivery

### Content Management
- **Project Showcase**: Organized display of AI Agents, Data Analysis, and Data Science projects
- **Service Offerings**: Detailed information about available services with pricing
- **Professional Profile**: About page with skills, education, and certifications

### Business Tools
- **Freelancing Platform**: Integrated booking system for freelance services
- **Contact Form**: Easy communication channel with email notifications
- **Admin Panel**: Content management system for easy updates
- **Chat Integration**: AI-powered chat assistant for instant responses

## 🚀 Deployment Options

### Production Platforms
- **Render** - Using the provided [render.yaml](render.yaml) configuration
- **Heroku** - Using the provided [Procfile](Procfile)
- **DigitalOcean** - Standard Django deployment
- **AWS** - Elastic Beanstalk deployment

### Deployment Configuration

#### Render Deployment
```yaml
# render.yaml
services:
  - type: web
    name: Freelancermrsingh
    env: python
    buildCommand: "chmod +x build.sh && PYTHON_VERSION=3.12 ./build.sh"
    startCommand: "PYTHON_VERSION=3.12 gunicorn portfolio_freelance.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.12.9
      - key: SECRET_KEY
        sync: false
      - key: DEBUG
        value: False
      - key: DB_NAME
        value: portfolio_db
      - key: DB_USER
        value: postgres
      - key: DB_HOST
        value: localhost
      - key: DB_PORT
        value: 5432
```

#### Heroku Deployment
```bash
# Procfile
web: gunicorn portfolio_freelance.wsgi:application --log-file -

# runtime.txt
python-3.12.9
```

#### Build Process
```bash
# build.sh
#!/usr/bin/env bash
set -o errexit

# Force Python 3.12
export PYTHON_VERSION=3.12
export PYENV_VERSION=3.12.9

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `SECRET_KEY` | Django secret key | Generated |
| `DEBUG` | Debug mode | `True` |
| `PYTHON_VERSION` | Python version | 3.12.9 |
| `DB_NAME` | PostgreSQL database name | portfolio_db |
| `DB_USER` | PostgreSQL username | postgres |
| `DB_PASSWORD` | PostgreSQL password |  |
| `DB_HOST` | PostgreSQL host | localhost |
| `DB_PORT` | PostgreSQL port | 5432 |
| `EMAIL_HOST_USER` | Gmail username | - |
| `EMAIL_HOST_PASSWORD` | Gmail app password | - |
| `GEMINI_API_KEY` | AI API key | - |

### Database Configuration

#### Development (SQLite)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### Production (PostgreSQL)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'portfolio_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

### Email Configuration

#### Development
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Portfolio Contact <tusharsinghoffical@gmail.com>'
CONTACT_EMAIL = 'tusharsinghoffical@gmail.com'
```

#### Production
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL')
```

## 📦 Development Setup

### Prerequisites
- Python 3.12.9
- pip package manager
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/Tusharsinghoffical/Website.github.io.git
cd Website.github.io

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

### Management Commands

```bash
# Run development server
python manage.py runserver

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Shell access
python manage.py shell

# View all available commands
python manage.py help
```

## 🎯 Services Offered

### Core Services
- **AI Agents Development**: Custom AI agents for workflow automation
- **Data Science Solutions**: Advanced analytics and machine learning models
- **Web Development**: Full-stack Python/Django applications
- **Data Analysis & Visualization**: Insights from complex datasets
- **Automation Solutions**: Process optimization through intelligent systems

### Specialized Offerings
- **Medical Website Development**: Secure healthcare platforms with patient portals
- **Food Delivery Platforms**: End-to-end food delivery solutions
- **Digital Marketing Solutions**: Comprehensive digital marketing services
- **AI-Powered Applications**: Intelligent applications with machine learning

## 🔧 Troubleshooting

### Common Issues

1. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic --no-input
   ```

2. **Database Migration Errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Email Configuration Issues**
   - Check DEBUG setting in settings.py
   - Verify EMAIL_HOST_PASSWORD for production
   - Enable 2FA and generate App Password for Gmail

4. **Deployment Failures**
   - Ensure all dependencies are in requirements.txt
   - Check runtime.txt for correct Python version
   - Verify build.sh has execute permissions

### Debugging Tips

- Check terminal output for error messages
- Use Django Debug Toolbar for development
- Enable verbose logging in settings.py
- Check browser developer tools for frontend issues

## 📞 Contact Information

For business inquiries or collaborations, feel free to reach out:

- **Email**: [tusharsinghkumar04@gmail.com](mailto:tusharsinghkumar04@gmail.com)
- **Phone**: [+91 8851619647](tel:+918851619647)
- **Website**: [https://codewithmrsingh.tech](https://codewithmrsingh.tech)

### Social Media
- **LinkedIn**: [Tushar Singh](https://www.linkedin.com/in/tusharsingh2011/)
- **GitHub**: [Tusharsinghoffical](https://github.com/Tusharsinghoffical)
- **YouTube**: [Code With Mr Singh](https://www.youtube.com/@codewithmrsingh4u)
- **Instagram**: [tusharsingh.dev](https://www.instagram.com/tusharsingh.dev/)
- **Topmate**: [Private Chat](https://topmate.io/tusharsinghoffical)

## 📄 License

© 2025 Tushar Singh. All rights reserved.

## 🔐 Admin Credentials

**Admin ID**: tusharsinghkumar2002
**Password**: Tushar@2002

## 📈 SEO & Analytics

### Meta Tags
- Comprehensive meta descriptions for all pages
- Keyword-rich content for better search rankings
- Open Graph tags for social sharing
- Twitter Card metadata

### Structured Data
- JSON-LD schema markup for Person and Organization
- Rich snippets for better search result appearance
- Proper canonical URLs to prevent duplicate content

### Performance Optimization
- Image optimization and lazy loading
- CSS/JS minification and compression
- Browser caching headers
- Gzip compression for faster loading