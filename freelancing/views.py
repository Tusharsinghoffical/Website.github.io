from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Booking, Payment, Service

def index(request):
    # Get services from database
    services = Service.objects.all()  # pyright: ignore[reportAttributeAccessIssue]
    
    # If no services exist, create default ones
    if not services.exists():
        services_data = [
            {
                'name': 'Medical Website Development',
                'description': 'Creating secure and compliant healthcare websites with patient portals and telemedicine features.',
                'price': 2500.00,
                'icon_class': 'fas fa-laptop-medical',
                'is_active': True
            },
            {
                'name': 'Food Delivery Platform',
                'description': 'Building end-to-end food delivery solutions with real-time tracking and payment integration.',
                'price': 3500.00,
                'icon_class': 'fas fa-utensils',
                'is_active': True
            },
            {
                'name': 'Digital Marketing Solutions',
                'description': 'Comprehensive digital marketing services to grow your online presence and customer base.',
                'price': 1500.00,
                'icon_class': 'fas fa-bullhorn',
                'is_active': True
            },
            {
                'name': 'AI Agents Development',
                'description': 'Developing intelligent AI agents and automation solutions for various business needs.',
                'price': 4000.00,
                'icon_class': 'fas fa-robot',
                'is_active': True
            }
        ]
        
        for service_data in services_data:
            Service.objects.create(**service_data)  # pyright: ignore[reportAttributeAccessIssue]
        
        services = Service.objects.all()  # pyright: ignore[reportAttributeAccessIssue]
    
    context = {
        'services': services,
    }
    
    return render(request, 'freelancing/index.html', context)

@csrf_exempt
def booking_submit(request):
    if request.method == 'POST':
        try:
            # Handle both JSON and form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
            
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone', '')
            service = data.get('service')
            preferred_date = data.get('date')
            preferred_time = data.get('time')
            message = data.get('message')
            budget = data.get('budget', None)
            
            # Validate required fields
            if not name or not email or not service or not preferred_date or not preferred_time or not message:
                return JsonResponse({'success': False, 'message': 'All required fields must be filled.'})
            
            # Validate email format
            if '@' not in email:
                return JsonResponse({'success': False, 'message': 'Please provide a valid email address.'})
            
            # Save to database
            booking = Booking(
                name=name,
                email=email,
                phone=phone,
                service=service,
                preferred_date=preferred_date,
                preferred_time=preferred_time,
                message=message,
                budget=budget if budget else None
            )
            booking.save()
            
            return JsonResponse({'success': True, 'message': 'Your booking has been submitted successfully! We will contact you shortly to confirm the details.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An error occurred while processing your booking. Please try again.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@csrf_exempt
def payment_process(request):
    if request.method == 'POST':
        try:
            # Handle both JSON and form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
            
            booking_id = data.get('booking_id')
            amount = data.get('amount')
            payment_method = data.get('payment_method')
            
            # Validate required fields
            if not booking_id or not amount or not payment_method:
                return JsonResponse({'success': False, 'message': 'All payment fields are required.'})
            
            # In a real application, you would integrate with a payment gateway here
            # For now, we'll just create a payment record and return a success message
            
            # Save payment to database
            payment = Payment(
                booking_id=booking_id,
                amount=amount,
                payment_method=payment_method,
                payment_status='completed'
            )
            payment.save()
            
            # Update booking status
            try:
                booking = Booking.objects.get(id=booking_id)  # pyright: ignore[reportAttributeAccessIssue]
                booking.status = 'confirmed'
                booking.save()
            except ObjectDoesNotExist:
                pass
            
            return JsonResponse({'success': True, 'message': 'Payment processed successfully! Thank you for your payment. Your booking is now confirmed.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'An error occurred while processing your payment. Please try again.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})