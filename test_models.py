import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_freelance.settings')
django.setup()

# Import models
from home.models import HomePageContent, Feature
from services.models import Service, ServiceCategory
from projects.models import Project, ProjectCategory
from about.models import Profile, SkillCategory, Skill
from contact.models import ContactMessage
from freelancing.models import Service as FreelanceService, Booking

def test_models():
    print("Testing Django models...")
    
    # Test Home models
    print("\n1. Testing Home models:")
    content = HomePageContent.objects.first()
    if content:
        print(f"   - Home content: {content.title}")
    else:
        print("   - No home content found")
    
    features = Feature.objects.all()
    print(f"   - Features count: {features.count()}")
    
    # Test Services models
    print("\n2. Testing Services models:")
    services = Service.objects.all()
    print(f"   - Services count: {services.count()}")
    
    categories = ServiceCategory.objects.all()
    print(f"   - Service categories count: {categories.count()}")
    
    # Test Projects models
    print("\n3. Testing Projects models:")
    projects = Project.objects.all()
    print(f"   - Projects count: {projects.count()}")
    
    # Test About models
    print("\n4. Testing About models:")
    profile = Profile.objects.first()
    if profile:
        print(f"   - Profile: {profile.name}")
    else:
        print("   - No profile found")
    
    skill_categories = SkillCategory.objects.all()
    print(f"   - Skill categories count: {skill_categories.count()}")
    
    skills = Skill.objects.all()
    print(f"   - Skills count: {skills.count()}")
    
    # Test Contact models
    print("\n5. Testing Contact models:")
    messages = ContactMessage.objects.all()
    print(f"   - Contact messages count: {messages.count()}")
    
    # Test Freelancing models
    print("\n6. Testing Freelancing models:")
    freelance_services = FreelanceService.objects.all()
    print(f"   - Freelance services count: {freelance_services.count()}")
    
    bookings = Booking.objects.all()
    print(f"   - Bookings count: {bookings.count()}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_models()