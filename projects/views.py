from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectCategory

def index(request):
    categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    
    # Get category filter from query parameters
    category_id = request.GET.get('category')
    if category_id:
        projects = projects.filter(category_id=category_id)
    
    context = {
        'categories': categories,
        'projects': projects,
        'selected_category': category_id,
    }
    return render(request, 'projects/index.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project,
    }
    return render(request, 'projects/detail.html', context)