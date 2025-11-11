from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
]