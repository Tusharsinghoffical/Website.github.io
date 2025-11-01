from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import ContactMessage

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
            
            return JsonResponse({'success': True, 'message': 'Your message has been sent successfully! We will get back to you soon.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An error occurred while sending your message. Please try again.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})