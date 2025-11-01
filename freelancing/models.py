from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    icon_class = models.CharField(max_length=50, default='fas fa-briefcase')
    is_active = models.BooleanField()
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    service = models.CharField(max_length=100)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.name) + " - " + str(self.service)
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['-created_at']

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "Payment for " + str(self.booking.name) + " - " + str(self.amount)
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"