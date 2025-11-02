from django.urls import path
from . import views

urlpatterns = [
    path('api/chat/', views.ChatView.as_view(), name='chat_api'),
    path('api/history/', views.chat_history, name='chat_history'),
]