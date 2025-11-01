from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
import json
import threading
from .models import ContactMessage

def send_email_async(subject, message, from_email, recipient_list):
    """Send email in a separate thread to avoid blocking the response"""
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
    except Exception as e:
        # Log the error but don't fail the request
        print(f"Email sending failed: {e}")

def index(request):
    return render(request, 'contact/index.html')

@csrf_exempt
def contact_submit(request):
    if request.method == 'POST':
        try:
            # Handle both JSON and form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
            
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            
            # Validate required fields
            if not name or not email or not subject or not message:
                return JsonResponse({'success': False, 'message': 'All fields are required.'})
            
            # Validate email format
            if '@' not in email:
                return JsonResponse({'success': False, 'message': 'Please provide a valid email address.'})
            
            # Save to database
            contact_message = ContactMessage(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            contact_message.save()
            
            # Send email notification asynchronously
            email_subject = f"New Contact Message: {subject}"
            email_message = f"""Hello,

You have received a new message from your website contact form.

----------------------------------------------------

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

----------------------------------------------------

This message has also been saved to your database.

Best regards,
Your Website Contact System
"""
            
            # Send email in a separate thread to avoid blocking the response
            email_thread = threading.Thread(
                target=send_email_async,
                args=(email_subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
            )
            email_thread.start()
            
            return JsonResponse({'success': True, 'message': 'Your message has been sent successfully! We will get back to you soon.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An error occurred while sending your message. Please try again.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})