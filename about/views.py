from django.shortcuts import render
from .models import Profile, SkillCategory, Skill, Education, Certification, Testimonial

def index(request):
    # Get profile from database
    profile = Profile.objects.first()  # type: ignore
    
    # If no profile exists, create a default one
    if not profile:
        profile = Profile.objects.create(  # type: ignore
            name='Tushar Singh',
            title='AI Agents Developer',
            bio='As a seasoned Data Scientist and AI Agents Developer, I specialize in transforming complex data into strategic business insights and developing intelligent automation systems that drive measurable results. With expertise in Python, Machine Learning, and cutting-edge AI technologies, I deliver tailored solutions that solve real-world challenges and create sustainable competitive advantages for businesses.',
            email='email@example.com',
            phone='+91 8851619647',
            location='City, Country'
        )
    
    # Get skills from database
    skill_categories = SkillCategory.objects.all()  # type: ignore
    
    # If no skill categories exist, create default ones
    if not skill_categories.exists():
        categories_data = [
            {'name': 'Programming Languages', 'order': 1},
            {'name': 'Frameworks & Libraries', 'order': 2},
            {'name': 'Databases', 'order': 3},
            {'name': 'Tools & Technologies', 'order': 4}
        ]
        
        for cat_data in categories_data:
            SkillCategory.objects.create(**cat_data)  # type: ignore
        
        skill_categories = SkillCategory.objects.all()  # type: ignore
    
    # Get skills for each category
    categories_with_skills = []
    for category in skill_categories:
        skills = Skill.objects.filter(category=category)  # type: ignore
        # If no skills exist for this category, create default ones
        if not skills.exists():
            if category.name == 'Programming Languages':
                skills_data = [
                    {'category': category, 'name': 'Python', 'proficiency_level': 95, 'order': 1},
                    {'category': category, 'name': 'JavaScript', 'proficiency_level': 85, 'order': 2},
                    {'category': category, 'name': 'SQL', 'proficiency_level': 90, 'order': 3}
                ]
            elif category.name == 'Frameworks & Libraries':
                skills_data = [
                    {'category': category, 'name': 'Django', 'proficiency_level': 90, 'order': 1},
                    {'category': category, 'name': 'React', 'proficiency_level': 85, 'order': 2},
                    {'category': category, 'name': 'TensorFlow', 'proficiency_level': 80, 'order': 3}
                ]
            elif category.name == 'Databases':
                skills_data = [
                    {'category': category, 'name': 'PostgreSQL', 'proficiency_level': 85, 'order': 1},
                    {'category': category, 'name': 'MongoDB', 'proficiency_level': 80, 'order': 2},
                    {'category': category, 'name': 'Redis', 'proficiency_level': 75, 'order': 3}
                ]
            else:  # Tools & Technologies
                skills_data = [
                    {'category': category, 'name': 'Docker', 'proficiency_level': 80, 'order': 1},
                    {'category': category, 'name': 'AWS', 'proficiency_level': 75, 'order': 2},
                    {'category': category, 'name': 'Git', 'proficiency_level': 90, 'order': 3}
                ]
            
            for skill_data in skills_data:
                Skill.objects.create(**skill_data)  # type: ignore
            
            skills = Skill.objects.filter(category=category)  # type: ignore
        
        category_dict = {
            'id': category.id,
            'name': category.name,
            'order': category.order,
            'skills': skills
        }
        categories_with_skills.append(category_dict)
    
    # Get education from database
    education = Education.objects.filter(profile=profile)  # type: ignore
    
    # If no education exists, create default ones
    if not education.exists():
        education_data = [
            {
                'profile': profile,
                'degree': 'Bachelor of Technology in Computer Science',
                'institution': 'University Name',
                'specialization': 'AI and Machine Learning',
                'start_date': '2018-07-01',
                'end_date': '2022-06-01',
                'is_current': False,
                'description': 'Focused on artificial intelligence, machine learning, and software development',
                'order': 1
            },
            {
                'profile': profile,
                'degree': 'Master of Technology in Data Science',
                'institution': 'University Name',
                'specialization': 'Advanced Data Analytics',
                'start_date': '2022-07-01',
                'end_date': None,
                'is_current': True,
                'description': 'Graduated with honors, specialized in AI and software development',
                'order': 2
            }
        ]
        
        for edu_data in education_data:
            Education.objects.create(**edu_data)  # type: ignore
        
        education = Education.objects.filter(profile=profile)  # type: ignore
    
    # Get certifications from database
    certifications = Certification.objects.filter(profile=profile)  # type: ignore
    
    # If no certifications exist, create default ones
    if not certifications.exists():
        certifications_data = [
            {
                'profile': profile,
                'name': 'AWS Certified Solutions Architect',
                'issuing_organization': 'Amazon Web Services',
                'issue_date': '2022-03-01',
                'credential_id': 'AWS-123456',
                'credential_url': '#',
                'order': 1
            },
            {
                'profile': profile,
                'name': 'Google Professional Data Engineer',
                'issuing_organization': 'Google Cloud',
                'issue_date': '2021-07-01',
                'credential_id': 'GCP-789012',
                'credential_url': '#',
                'order': 2
            }
        ]
        
        for cert_data in certifications_data:
            Certification.objects.create(**cert_data)  # type: ignore
        
        certifications = Certification.objects.filter(profile=profile)  # type: ignore
    
    # Get testimonials from database
    testimonials = Testimonial.objects.filter(profile=profile)  # type: ignore
    
    # If no testimonials exist, create the specific ones you requested
    if not testimonials.exists():
        testimonials_data = [
            # Medical Website Project
            {
                'profile': profile,
                'client_name': 'Dr. Anjali Mehta',
                'client_company': 'MediCare Hospitals',
                'client_location': 'Delhi, India',
                'client_type': 'indian',
                'rating': 5,
                'testimonial_text': 'Tushar developed a comprehensive medical website for our hospital chain with patient portal, appointment booking, and telemedicine features. The website has significantly improved our patient engagement and reduced administrative workload. His attention to healthcare compliance standards was impressive.',
                'project_name': 'Medical Website Development for Healthcare Portal',
                'date': '2025-10-15',
                'order': 1,
                'is_featured': True
            },
            # AI Agent Project
            {
                'profile': profile,
                'client_name': 'Rajiv Sharma',
                'client_company': 'TechFlow Solutions',
                'client_location': 'Mumbai, India',
                'client_type': 'indian',
                'rating': 5,
                'testimonial_text': 'The AI agent Tushar built for our customer support system has revolutionized our operations. It handles over 80% of routine queries automatically, freeing up our human agents for complex issues. The natural language processing capabilities are exceptional.',
                'project_name': 'AI Agent for Customer Support Automation',
                'date': '2025-09-22',
                'order': 2,
                'is_featured': True
            },
            # Restaurant System Project
            {
                'profile': profile,
                'client_name': 'Vikram Patel',
                'client_company': 'FoodExpress Chain',
                'client_location': 'Bangalore, India',
                'client_type': 'indian',
                'rating': 4,
                'testimonial_text': 'Tushar created a complete restaurant management system for our chain of outlets. The system handles order management, inventory tracking, staff scheduling, and customer loyalty programs. It has streamlined our operations and improved customer satisfaction significantly.',
                'project_name': 'Restaurant Management System with Delivery Integration',
                'date': '2025-08-30',
                'order': 3,
                'is_featured': True
            },
            # IPO Project
            {
                'profile': profile,
                'client_name': 'Priya Krishnan',
                'client_company': 'FinTech Innovations Ltd',
                'client_location': 'Chennai, India',
                'client_type': 'indian',
                'rating': 5,
                'testimonial_text': 'For our company\'s IPO preparation, Tushar developed a sophisticated financial data analysis platform that helped us present our growth metrics effectively to potential investors. The real-time dashboard and predictive modeling features were crucial in our successful public offering.',
                'project_name': 'IPO Preparation - Financial Data Analysis Platform',
                'date': '2025-11-05',
                'order': 4,
                'is_featured': True
            },
            # Thumbnail Design Project
            {
                'profile': profile,
                'client_name': 'David Wilson',
                'client_company': 'Global Media Corp',
                'client_location': 'New York, USA',
                'client_type': 'foreign',
                'rating': 5,
                'testimonial_text': 'Tushar\'s creative thumbnail designs for our YouTube channel increased our click-through rates by 65%. His understanding of visual psychology and platform algorithms resulted in a significant boost to our subscriber count and engagement metrics.',
                'project_name': 'Thumbnail Design for Digital Marketing Campaign',
                'date': '2025-10-28',
                'order': 5,
                'is_featured': True
            }
        ]
        
        for testimonial_data in testimonials_data:
            Testimonial.objects.create(**testimonial_data)  # type: ignore
        
        testimonials = Testimonial.objects.filter(profile=profile)  # type: ignore
    
    context = {
        'profile': profile,
        'skill_categories': categories_with_skills,
        'education': education,
        'certifications': certifications,
        'testimonials': testimonials,
    }
    
    return render(request, 'about/index.html', context)