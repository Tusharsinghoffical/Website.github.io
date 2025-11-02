from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='freelancing'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('booking/', views.booking_submit, name='booking_submit'),
    path('payment/', views.payment_process, name='payment_process'),
]