from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import About, Home, SocialMedia, Skills, Project, Images, ContactMessage, ProjectRating

def index(request):
    home = Home.objects.get()
    social_media = SocialMedia.objects.order_by('id')
    about = About.objects.get()
    projects = Project.objects.order_by('id')
    skills = Skills.objects.order_by('id')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # Save the message in the database
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            # Show a success message
            messages.success(request, 'Your message has been sent successfully! I will contact you soon.')
            return redirect('index')
        else:
            messages.error(request, 'Please fill out all required fields.')
        
    for project in projects:
        try:
            project.first_image = project.images_set.first()
        except:
            project.first_image = None
            
    return render(
        request, 'index.html',
        {
            'home': home,
            'social_media': social_media,
            'about': about,
            'projects': projects,
            'skills': skills
        }
    )


def project_detail(request, pid):
    project = get_object_or_404(Project, id=pid)
    project_images = Images.objects.filter(project=project)
    project_skills = Skills.objects.filter(project=project)
    return render(
        request, 'project.html',
        {
            'project': project,
            'project_images': project_images,
            'project_skills': project_skills
        }
    )


def rate_project(request, pid):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=pid)
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        message = request.POST.get('message')
        
        if name and rating and message:
            # Save the evaluation in the database
            ProjectRating.objects.create(
                project=project,
                name=name,
                rating=int(rating),
                message=message
            )
            messages.success(request, 'Thank you for your rating!')
        else:
            messages.error(request, 'Please fill out all required fields.')
            
    return redirect('project_detail', pid=pid)
