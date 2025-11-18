from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
import json
from decimal import Decimal
from datetime import datetime
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

def service_detail(request, service_id):
    # Get the specific service
    service = get_object_or_404(Service, id=service_id)  # pyright: ignore[reportAttributeAccessIssue]
    
    # Get all services for the booking modal
    services = Service.objects.all()  # pyright: ignore[reportAttributeAccessIssue]
    
    context = {
        'service': service,
        'services': services,
    }
    
    return render(request, 'freelancing/service_detail.html', context)

@csrf_exempt
def booking_submit(request):
    if request.method == 'POST':
        try:
            # Handle both JSON and form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
            
            print("Booking data received:", data)  # Debug print
            
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
            
            # Parse date and time properly
            try:
                # Convert date string to date object
                if isinstance(preferred_date, str):
                    # Try multiple date formats
                    date_formats = ['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y']
                    parsed_date = None
                    for fmt in date_formats:
                        try:
                            parsed_date = datetime.strptime(preferred_date, fmt).date()
                            break
                        except ValueError:
                            continue
                    
                    if parsed_date is None:
                        return JsonResponse({'success': False, 'message': 'Invalid date format. Please use YYYY-MM-DD, DD-MM-YYYY, or MM/DD/YYYY format.'})
                else:
                    parsed_date = preferred_date
            except Exception as e:
                print(f"Date parsing error: {e}")
                return JsonResponse({'success': False, 'message': 'Invalid date format. Please use YYYY-MM-DD, DD-MM-YYYY, or MM/DD/YYYY format.'})
            
            try:
                # Convert time string to time object
                if isinstance(preferred_time, str):
                    # Handle time format: HH:MM
                    parsed_time = datetime.strptime(preferred_time, '%H:%M').time()
                else:
                    parsed_time = preferred_time
            except Exception as e:
                print(f"Time parsing error: {e}")
                return JsonResponse({'success': False, 'message': 'Invalid time format. Please use HH:MM format.'})
            
            # Parse budget if provided
            parsed_budget = None
            if budget:
                try:
                    if isinstance(budget, str):
                        parsed_budget = Decimal(budget)
                    else:
                        parsed_budget = budget
                except Exception as e:
                    print(f"Budget parsing error: {e}")
                    # Don't fail if budget parsing fails, just set to None
                    parsed_budget = None
            
            # Save to database
            booking = Booking(
                name=name,
                email=email,
                phone=phone,
                service=service,
                preferred_date=parsed_date,
                preferred_time=parsed_time,
                message=message,
                budget=parsed_budget
            )
            booking.save()
            
            print("Booking saved to database")  # Debug print
            
            # Send email notification
            try:
                subject = f"New Booking Request: {service}"
                message_body = f"""
New Booking Request Details:

Name: {name}
Email: {email}
Phone: {phone if phone else 'Not provided'}
Service: {service}
Preferred Date: {preferred_date}
Preferred Time: {preferred_time}
Budget: {budget if budget else 'Not specified'}

Project Details:
{message}

Please follow up with the client as soon as possible.
                """
                
                print("Sending email to:", settings.CONTACT_EMAIL)  # Debug print
                
                send_mail(
                    subject=subject,
                    message=message_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                print("Email sent successfully")  # Debug print
            except Exception as e:
                # Log the error but don't fail the request
                print(f"Email sending failed: {e}")
            
            return JsonResponse({'success': True, 'message': 'Your booking has been submitted successfully! We will contact you shortly to confirm the details.'})
        except Exception as e:
            print(f"Booking submission error: {e}")  # Debug print
            import traceback
            traceback.print_exc()  # Print full traceback for debugging
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