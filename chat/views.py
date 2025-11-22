import json
import uuid
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.conf import settings
from .models import ChatSession, ChatMessage

class ChatView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            session_id = data.get('session_id', None)
            
            # Create or get session
            if not session_id:
                session_id = str(uuid.uuid4())
                chat_session = ChatSession.objects.create(session_id=session_id)  # type: ignore
            else:
                try:
                    chat_session = ChatSession.objects.get(session_id=session_id)  # type: ignore
                except ChatSession.DoesNotExist:  # type: ignore
                    chat_session = ChatSession.objects.create(session_id=session_id)  # type: ignore
            
            # Save user message
            ChatMessage.objects.create(  # type: ignore
                session=chat_session,
                message_type='user',
                content=user_message
            )
            
            # Generate bot response using AI
            bot_response = self.generate_ai_response(user_message, chat_session)
            
            # Save bot message
            ChatMessage.objects.create(  # type: ignore
                session=chat_session,
                message_type='bot',
                content=bot_response
            )
            
            return JsonResponse({
                'session_id': session_id,
                'response': bot_response
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def generate_ai_response(self, user_message, chat_session):
        """
        Generate AI response using Google Gemini API or fallback to rule-based
        """
        try:
            # Get chat history for context
            messages = chat_session.messages.all().order_by('timestamp')
            
            # Build conversation history for Gemini
            conversation_history = []
            
            # Add previous messages to context
            for msg in messages:
                if msg.message_type == 'user':
                    conversation_history.append({"role": "user", "parts": [{"text": msg.content}]})
                elif msg.message_type == 'bot':
                    conversation_history.append({"role": "model", "parts": [{"text": msg.content}]})
            
            # Add current user message
            conversation_history.append({"role": "user", "parts": [{"text": user_message}]})
            
            # Try to use Google Gemini API
            if hasattr(settings, 'GEMINI_API_KEY') and settings.GEMINI_API_KEY:
                gemini_api_key = settings.GEMINI_API_KEY
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api_key}"
                
                # Prepare the payload
                payload = {
                    "contents": conversation_history,
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 300
                    }
                }
                
                # Make the API request
                headers = {'Content-Type': 'application/json'}
                response = requests.post(url, json=payload, headers=headers)
                
                if response.status_code == 200:
                    result = response.json()
                    if 'candidates' in result and len(result['candidates']) > 0:
                        candidate = result['candidates'][0]
                        if 'content' in candidate and 'parts' in candidate['content']:
                            return candidate['content']['parts'][0]['text'].strip()
                
                # If we get here, there was an issue with the API response
                raise Exception(f"Gemini API returned status {response.status_code}")
            else:
                # Fallback to rule-based response if no API key
                return self.generate_rule_based_response(user_message)
                
        except Exception as e:
            # Fallback to rule-based response if API fails
            print(f"AI API error: {e}")
            return self.generate_rule_based_response(user_message)
    
    def generate_rule_based_response(self, user_message):
        """
        Simple rule-based response generator as fallback with improved formatting
        """
        user_message = user_message.lower()
        
        if 'hello' in user_message or 'hi' in user_message or 'hey' in user_message:
            return ("Hello! 👋 I'm your AI assistant.\n\n"
                    "I can help you with information about:\n"
                    "• Services we offer\n"
                    "• Projects we've completed\n"
                    "• Contact details\n"
                    "• Freelancing opportunities\n\n"
                    "How can I assist you today?")
        
        elif 'service' in user_message:
            return ("We offer a range of professional services:\n\n"
                    "🔧 Web Development\n"
                    "• Custom websites and web applications\n"
                    "• E-commerce solutions\n"
                    "• Responsive design for all devices\n\n"
                    "🤖 AI & Machine Learning\n"
                    "• Intelligent chatbots\n"
                    "• Data analysis and visualization\n"
                    "• Predictive modeling\n\n"
                    "📊 Data Science\n"
                    "• Business intelligence solutions\n"
                    "• Statistical analysis\n"
                    "• Data cleaning and preprocessing\n\n"
                    "Would you like more details about any specific service?")
        
        elif 'project' in user_message:
            return ("We have worked on several exciting projects:\n\n"
                    "🌐 Portfolio & Freelancing Platform\n"
                    "• Full-stack Django web application\n"
                    "• Responsive design with Bootstrap\n"
                    "• Integrated AI chatbot functionality\n\n"
                    "🤖 AI Chatbot Solutions\n"
                    "• Conversational interfaces for businesses\n"
                    "• Integration with multiple AI APIs\n"
                    "• Persistent chat history\n\n"
                    "📈 Data Analysis Dashboards\n"
                    "• Interactive data visualization\n"
                    "• Real-time analytics\n"
                    "• Custom reporting tools\n\n"
                    "You can view our complete portfolio in the Projects section of our website.")
        
        elif 'contact' in user_message:
            return ("You can reach us through multiple channels:\n\n"
                    "📧 Email: tusharsinghoffical@gmail.com\n"
                    "📱 Phone: +91 8851619647\n"
                    "📍 Location: Delhi, India\n\n"
                    "🌐 Online:\n"
                    "• Fill out the contact form on our website\n"
                    "• Connect on LinkedIn: linkedin.com/in/tusharsingh2011\n"
                    "• Follow us on GitHub: github.com/Tusharsinghoffical\n\n"
                    "We typically respond within 24 hours.")
        
        elif 'freelance' in user_message or 'work' in user_message:
            return ("We offer professional freelancing services:\n\n"
                    "💼 What we provide:\n"
                    "• Custom software development\n"
                    "• AI and machine learning solutions\n"
                    "• Data analysis and visualization\n"
                    "• Website and application development\n\n"
                    "⚡ Why choose us:\n"
                    "• 5+ years of experience\n"
                    "• Expertise in Python, Django, and AI\n"
                    "• Fast turnaround times\n"
                    "• Competitive pricing\n\n"
                    "Visit our Freelancing section to submit a project request or get a quote.")
        
        elif 'about' in user_message or 'yourself' in user_message:
            return ("I'm glad you asked about us!\n\n"
                    "👨‍💻 Tushar Singh - AI & Data Science Specialist\n"
                    "• Expertise in Python, Machine Learning, and AI Agents\n"
                    "• Professional web development with Django\n"
                    "• Data analysis and visualization specialist\n"
                    "• Passionate about creating smart, efficient solutions\n\n"
                    "🎓 Background:\n"
                    "• Data Scientist with focus on AI applications\n"
                    "• Experience in building intelligent AI agents\n"
                    "• Transforming complex data into actionable insights\n\n"
                    "Check out our About section for more detailed information.")
        
        elif 'thank' in user_message:
            return ("You're very welcome! 😊\n\n"
                    "I'm here to help whenever you need information about:\n"
                    "• Our services and expertise\n"
                    "• Completed projects and case studies\n"
                    "• Contact information and availability\n"
                    "• Freelancing opportunities\n\n"
                    "Is there anything else I can assist you with?")
        
        elif 'bye' in user_message or 'goodbye' in user_message:
            return ("Goodbye! 👋\n\n"
                    "Thank you for chatting with me today.\n\n"
                    "Feel free to return anytime if you have more questions.\n"
                    "Have a wonderful day!")
        
        elif 'help' in user_message:
            return ("I'm here to help you navigate our services and information:\n\n"
                    "You can ask me about:\n"
                    "• Services we offer\n"
                    "• Projects we've completed\n"
                    "• Contact information\n"
                    "• Freelancing opportunities\n"
                    "• About our team\n\n"
                    "Just let me know what you'd like to learn more about!")
        
        else:
            responses = [
                ("I understand you're interested in our services.\n\n"
                 "To help you better, you could ask about:\n"
                 "• Specific services we offer\n"
                 "• Projects we've completed\n"
                 "• How to contact us\n"
                 "• Freelancing opportunities\n\n"
                 "What would you like to know more about?"),
                
                ("That's an interesting question!\n\n"
                 "Our team specializes in:\n"
                 "• AI solutions and machine learning\n"
                 "• Web development with Python/Django\n"
                 "• Data science and analysis\n\n"
                 "Would you like details about any of these areas?"),
                
                ("Thanks for your inquiry!\n\n"
                 "One of our experts will get back to you shortly.\n"
                 "In the meantime, I can provide information about:\n"
                 "• Our service offerings\n"
                 "• Past projects and case studies\n"
                 "• Contact methods\n\n"
                 "What would you like to know?"),
                
                ("I'm here to help you with any questions!\n\n"
                 "Popular topics include:\n"
                 "• Web development services\n"
                 "• AI and machine learning solutions\n"
                 "• Data analysis capabilities\n"
                 "• Portfolio of completed projects\n\n"
                 "What specific information are you looking for?"),
                
                ("I'd be happy to assist you better!\n\n"
                 "Could you provide more details about your requirements?\n"
                 "For example:\n"
                 "• What type of project you have in mind\n"
                 "• What services you're interested in\n"
                 "• Any specific timeline or budget considerations\n\n"
                 "This will help me give you more targeted information.")
            ]
            import random
            return random.choice(responses)

# API endpoint to get chat history
@csrf_exempt
def chat_history(request):
    try:
        data = json.loads(request.body)
        session_id = data.get('session_id', None)
        
        if not session_id:
            return JsonResponse({'messages': []})
        
        try:
            chat_session = ChatSession.objects.get(session_id=session_id)  # type: ignore
            messages = chat_session.messages.all()
            message_list = [
                {
                    'type': msg.message_type,
                    'content': msg.content,
                    'timestamp': msg.timestamp.isoformat()
                }
                for msg in messages
            ]
            return JsonResponse({'messages': message_list})
        except ChatSession.DoesNotExist:  # type: ignore
            return JsonResponse({'messages': []})
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)