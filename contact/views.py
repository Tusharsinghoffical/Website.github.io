from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
import json
import threading
import logging
from .models import ContactMessage

# Set up logging
logger = logging.getLogger(__name__)

def send_email_async(subject, message, from_email, recipient_list):
    """Send email in a separate thread to avoid blocking the response"""
    try:
        # Check if required email settings are available
        if not hasattr(settings, 'EMAIL_HOST_USER') or not settings.EMAIL_HOST_USER:
            logger.warning("Email settings not configured properly")
            return
            
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
    except Exception as e:
        # Log the error but don't fail the request
        logger.error(f"Email sending failed: {e}")

def index(request):
    try:
        # You can pass dynamic contact information here if needed
        context = {
            'email': 'tusharsinghkumar04@gmail.com',
            'phone': '+91 8851619647',
            'location': 'Delhi, India'
        }
        return render(request, 'contact/index.html', context)
    except Exception as e:
        logger.error(f"Contact page error: {e}", exc_info=True)
        raise

@csrf_exempt
def contact_submit(request):
    logger.info("Contact form submission started")
    if request.method == 'POST':
        try:
            logger.info("Processing POST request")
            # Handle both JSON and form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                logger.info("Received JSON data")
            else:
                data = request.POST
                logger.info("Received form data")
            
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            subject = data.get('subject')
            message = data.get('message')
            
            logger.info(f"Form data: name={name}, email={email}, subject={subject}")
            
            # Validate required fields
            if not name or not email or not subject or not message:
                logger.warning("Missing required fields")
                return JsonResponse({'success': False, 'message': 'All fields are required.'})
            
            # Validate email format
            if '@' not in email:
                logger.warning("Invalid email format")
                return JsonResponse({'success': False, 'message': 'Please provide a valid email address.'})
            
            # Save to database
            logger.info("Saving to database")
            contact_message = ContactMessage(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            contact_message.save()
            logger.info("Successfully saved to database")
            
            # Send email notification asynchronously
            email_subject = f"Message from the website: {subject}"
            email_message = f"""
Subject: {subject}

{message}

Best regards,
Name: {name}
Email: {email}
Phone: {phone if phone else 'Not provided'}
"""
            
            logger.info("Preparing to send email")
            # Check if email settings are properly configured
            if not hasattr(settings, 'CONTACT_EMAIL') or not settings.CONTACT_EMAIL:
                logger.warning("CONTACT_EMAIL not configured, skipping email notification")
            else:
                logger.info(f"Sending email to {settings.CONTACT_EMAIL}")
                # Send email in a separate thread to avoid blocking the response
                email_thread = threading.Thread(
                    target=send_email_async,
                    args=(email_subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
                )
                email_thread.start()
            
            logger.info("Contact form submission completed successfully")
            return JsonResponse({'success': True, 'message': 'Your message has been sent successfully! We will get back to you soon.'})
        except Exception as e:
            logger.error(f"Contact form submission error: {e}", exc_info=True)
            return JsonResponse({'success': False, 'message': 'An error occurred while sending your message. Please try again.'})
    
    logger.warning("Invalid request method")
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
