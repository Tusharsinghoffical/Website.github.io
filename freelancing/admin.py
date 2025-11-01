from django.contrib import admin
from .models import Service, Booking, Payment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'preferred_date', 'status', 'created_at')
    list_filter = ('service', 'status', 'created_at')
    search_fields = ('name', 'email', 'service')
    ordering = ('-created_at',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_method', 'payment_status', 'created_at')
    list_filter = ('payment_method', 'payment_status', 'created_at')
    search_fields = ('booking__name', 'transaction_id')
    ordering = ('-created_at',)