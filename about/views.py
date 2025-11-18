from django.shortcuts import render
from .models import Profile, SkillCategory, Skill, Education, Certification

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
        
        for category_data in categories_data:
            SkillCategory.objects.create(**category_data)  # type: ignore
        
        skill_categories = SkillCategory.objects.all()  # type: ignore
    
    # Add skills to each category (without direct assignment)
    categories_with_skills = []
    for category in skill_categories:
        category_dict = {
            'id': category.id,
            'name': category.name,
            'order': category.order,
            'skills': Skill.objects.filter(category=category)  # type: ignore
        }
        categories_with_skills.append(category_dict)
    
    # If no skills exist, create default ones
    if not Skill.objects.exists():  # type: ignore
        skills_data = [
            # Programming Languages
            {'category_id': 1, 'name': 'Python', 'proficiency_level': 95, 'order': 1},
            {'category_id': 1, 'name': 'JavaScript', 'proficiency_level': 85, 'order': 2},
            {'category_id': 1, 'name': 'SQL', 'proficiency_level': 90, 'order': 3},
            
            # Frameworks & Libraries
            {'category_id': 2, 'name': 'Django', 'proficiency_level': 90, 'order': 1},
            {'category_id': 2, 'name': 'React', 'proficiency_level': 85, 'order': 2},
            {'category_id': 2, 'name': 'TensorFlow', 'proficiency_level': 80, 'order': 3},
            
            # Databases
            {'category_id': 3, 'name': 'PostgreSQL', 'proficiency_level': 85, 'order': 1},
            {'category_id': 3, 'name': 'MongoDB', 'proficiency_level': 80, 'order': 2},
            {'category_id': 3, 'name': 'Redis', 'proficiency_level': 75, 'order': 3},
            
            # Tools & Technologies
            {'category_id': 4, 'name': 'Docker', 'proficiency_level': 80, 'order': 1},
            {'category_id': 4, 'name': 'AWS', 'proficiency_level': 75, 'order': 2},
            {'category_id': 4, 'name': 'Git', 'proficiency_level': 90, 'order': 3}
        ]
        
        for skill_data in skills_data:
            Skill.objects.create(**skill_data)  # type: ignore
        
        # Refresh categories with skills
        categories_with_skills = []
        for category in SkillCategory.objects.all():  # type: ignore
            category_dict = {
                'id': category.id,
                'name': category.name,
                'order': category.order,
                'skills': Skill.objects.filter(category=category)  # type: ignore
            }
            categories_with_skills.append(category_dict)
    
    # Get education from database
    education = Education.objects.filter(profile=profile)  # type: ignore
    
    # If no education exists, create default ones
    if not education.exists():
        education_data = [
            {
                'profile': profile,
                'degree': 'Master of Science in Data Science',
                'institution': 'University of Technology',
                'specialization': 'Machine Learning',
                'start_date': '2020-09-01',
                'end_date': '2022-06-01',
                'is_current': False,
                'description': 'Focused on machine learning algorithms and big data analytics',
                'order': 1
            },
            {
                'profile': profile,
                'degree': 'Bachelor of Technology in Computer Science',
                'institution': 'Institute of Engineering',
                'specialization': 'Artificial Intelligence',
                'start_date': '2016-09-01',
                'end_date': '2020-06-01',
                'is_current': False,
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
    
    context = {
        'profile': profile,
        'skill_categories': categories_with_skills,
        'education': education,
        'certifications': certifications,
    }
    
    return render(request, 'about/index.html', context)