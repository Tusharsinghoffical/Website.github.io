from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contact'),
    path('submit/', views.contact_submit, name='contact_submit'),
]