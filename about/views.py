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
    
    # If no testimonials exist, create default ones
    if not testimonials.exists():
        testimonials_data = [
            # Indian clients
            {
                'profile': profile,
                'client_name': 'Rajesh Kumar',
                'client_company': 'TechInnovate Solutions',
                'client_location': 'Mumbai, India',
                'client_type': 'indian',
                'rating': 5,
                'testimonial_text': 'Tushar delivered an exceptional AI chatbot solution for our customer support system. His expertise in natural language processing and machine learning significantly improved our response times and customer satisfaction scores. Highly recommended for any AI projects!',
                'project_name': 'AI-Powered Customer Support Chatbot',
                'date': '2025-09-15',
                'order': 1,
                'is_featured': True
            },
            {
                'profile': profile,
                'client_name': 'Priya Sharma',
                'client_company': 'DataDriven Analytics',
                'client_location': 'Bangalore, India',
                'client_type': 'indian',
                'rating': 5,
                'testimonial_text': 'Working with Tushar was a game-changer for our business. He developed a predictive analytics model that helped us optimize our supply chain operations, resulting in a 30% cost reduction. His technical skills combined with clear communication made the entire process seamless.',
                'project_name': 'Supply Chain Optimization with Predictive Analytics',
                'date': '2025-08-22',
                'order': 2,
                'is_featured': True
            },
            {
                'profile': profile,
                'client_name': 'Amit Patel',
                'client_company': 'HealthTech Innovations',
                'client_location': 'Delhi, India',
                'client_type': 'indian',
                'rating': 4,
                'testimonial_text': 'Tushar created a comprehensive healthcare dashboard for our telemedicine platform. The real-time analytics and patient monitoring features have been instrumental in improving our service quality. His attention to detail and commitment to deadlines are impressive.',
                'project_name': 'Telemedicine Analytics Dashboard',
                'date': '2025-07-30',
                'order': 3,
                'is_featured': False
            },
            {
                'profile': profile,
                'client_name': 'Sneha Gupta',
                'client_company': 'FinEdge Solutions',
                'client_location': 'Pune, India',
                'client_type': 'indian',
                'rating': 5,
                'testimonial_text': 'We hired Tushar to develop a fraud detection system for our fintech platform. His machine learning approach was innovative and highly effective, reducing fraudulent transactions by 85%. He provided excellent documentation and training for our team.',
                'project_name': 'AI-Based Fraud Detection System',
                'date': '2025-10-05',
                'order': 4,
                'is_featured': True
            },
            # Foreign client
            {
                'profile': profile,
                'client_name': 'Michael Johnson',
                'client_company': 'GlobalTech Solutions',
                'client_location': 'San Francisco, USA',
                'client_type': 'foreign',
                'rating': 5,
                'testimonial_text': 'Tushar\'s expertise in AI agents development transformed our business operations. The automation solutions he built for our data processing pipeline saved us over 200 hours per month. His professionalism and technical depth are outstanding. Will definitely work with him again.',
                'project_name': 'Enterprise Data Processing Automation',
                'date': '2025-09-28',
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