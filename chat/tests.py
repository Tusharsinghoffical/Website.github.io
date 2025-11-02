from django.test import TestCase, Client
from django.urls import reverse
from .models import ChatSession, ChatMessage
import json

class ChatViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.session_id = 'test_session_123'
        
    def test_chat_api_post(self):
        """Test the chat API endpoint"""
        url = reverse('chat_api')
        data = {
            'message': 'Hello, AI assistant!',
            'session_id': self.session_id
        }
        
        response = self.client.post(
            url, 
            json.dumps(data), 
            content_type='application/json'
        )
        
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check that the response contains the expected keys
        response_data = json.loads(response.content)
        self.assertIn('session_id', response_data)
        self.assertIn('response', response_data)
        
        # Check that the session was created
        session = ChatSession.objects.get(session_id=self.session_id)
        self.assertIsNotNone(session)
        
        # Check that messages were saved
        messages = ChatMessage.objects.filter(session=session)
        self.assertEqual(messages.count(), 2)  # User message and bot response
        
        # Check message types
        user_message = messages.get(message_type='user')
        bot_message = messages.get(message_type='bot')
        
        self.assertEqual(user_message.content, 'Hello, AI assistant!')
        self.assertIsNotNone(bot_message.content)
        
    def test_chat_history(self):
        """Test the chat history endpoint"""
        # First, create a session and messages
        session = ChatSession.objects.create(session_id=self.session_id)
        ChatMessage.objects.create(
            session=session,
            message_type='user',
            content='Hello!'
        )
        ChatMessage.objects.create(
            session=session,
            message_type='bot',
            content='Hi there!'
        )
        
        # Test the history endpoint
        url = reverse('chat_history')
        data = {'session_id': self.session_id}
        
        response = self.client.post(
            url,
            json.dumps(data),
            content_type='application/json'
        )
        
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check the response content
        response_data = json.loads(response.content)
        self.assertIn('messages', response_data)
        self.assertEqual(len(response_data['messages']), 2)