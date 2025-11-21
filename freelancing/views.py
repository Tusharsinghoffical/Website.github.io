from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
import json
import logging
from decimal import Decimal
from datetime import datetime
import re
from .models import Booking, Payment, Service

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    services = Service.objects.all()
    return render(request, 'freelancing/index.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'freelancing/service_detail.html', {'service': service})

@csrf_exempt
def booking_submit(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Get service name from form data
            service_name = data.get('service')
            if not service_name:
                return JsonResponse({'success': False, 'message': 'Service is required.'})
            
            # Parse date with multiple format support
            date_str = data.get('date')
            if not date_str:
                return JsonResponse({'success': False, 'message': 'Date is required.'})
            
            # Try multiple date formats
            parsed_date = None
            date_formats = ['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y']
            for fmt in date_formats:
                try:
                    parsed_date = datetime.strptime(date_str, fmt).date()
                    break
                except ValueError:
                    continue
            
            if parsed_date is None:
                return JsonResponse({'success': False, 'message': 'Invalid date format. Please use YYYY-MM-DD, DD-MM-YYYY, or MM/DD/YYYY.'})
            
            # Parse time
            time_str = data.get('time')
            if not time_str:
                return JsonResponse({'success': False, 'message': 'Time is required.'})
            
            try:
                parsed_time = datetime.strptime(time_str, '%H:%M').time()
            except ValueError:
                return JsonResponse({'success': False, 'message': 'Invalid time format. Please use HH:MM (24-hour format).'}) 
            
            # Process booking data
            booking = Booking.objects.create(
                name=data['name'],
                email=data['email'],
                phone=data.get('phone', ''),
                service=service_name,
                preferred_date=parsed_date,
                preferred_time=parsed_time,
                message=data.get('message', ''),
                budget=Decimal(data.get('budget')) if data.get('budget') else None,
                status='pending',
                created_at=timezone.now()
            )
            
            # Send confirmation email
            try:
                send_mail(
                    'Booking Confirmation',
                    f'Thank you for your booking, {data["name"]}. We will contact you soon.\n\nBooking Details:\nService: {service_name}\nDate: {date_str}\nTime: {time_str}',
                    settings.DEFAULT_FROM_EMAIL,
                    [data['email']],
                    fail_silently=False,
                )
            except Exception as e:
                logger.error(f"Failed to send email: {e}")
            
            return JsonResponse({'success': True, 'message': 'Booking submitted successfully'})
        except Exception as e:
            logger.error(f"Booking submission error: {e}")
            return JsonResponse({'success': False, 'message': 'Error submitting booking. Please try again.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
def payment_process(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Process payment data
            payment = Payment.objects.create(
                amount=Decimal(data['amount']),
                payment_method=data['payment_method'],
                payment_status='pending',
                created_at=timezone.now()
            )
            return JsonResponse({'success': True, 'message': 'Payment processed successfully', 'payment_id': payment.id})
        except Exception as e:
            logger.error(f"Payment processing error: {e}")
            return JsonResponse({'success': False, 'message': 'Error processing payment. Please try again.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})