# core/views.py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Contact



def home(request):
    context = {
        # Your existing context data
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

# def contact(request):
#     return render(request, 'core/contact.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project_type = request.POST.get('project_type')
        location = request.POST.get('location')
        budget = request.POST.get('budget')
        message = request.POST.get('message')

        # Save to PostgreSQL
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            project_type=project_type,
            location=location,
            budget=budget,
            message=message
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'core/contact.html')

def portfolio(request):
    # Sample project data - in a real application, you would fetch this from a database
    projects = [
        {
            'id': 1,
            'title': 'Modern Residential Villa',
            'category': 'residential',
            'description': 'A luxurious 4-bedroom villa with modern amenities and sustainable design features. This project featured energy-efficient solutions and smart home technology integration.',
            'location': 'New York, NY',
            'area': '3200 sq ft',
            'duration': '12',
            'completion_date': 'June 2023',
            'image': '/static/images/projects/villa.jpg',
            'gallery_images': [
                '/static/images/projects/villa-1.jpg',
                '/static/images/projects/villa-2.jpg',
                '/static/images/projects/villa-3.jpg',
            ],
            'features': ['Smart Home Automation', 'Solar Panel Installation', 'Energy-Efficient Windows', 'Custom Kitchen Design']
        },
        # ... other projects ...
    ]
    
    # Get filter parameter from URL
    category_filter = request.GET.get('category', 'all')
    
    # Filter projects if a category is selected
    if category_filter != 'all':
        filtered_projects = [p for p in projects if p['category'] == category_filter]
    else:
        filtered_projects = projects
    
    # Pagination
    paginator = Paginator(filtered_projects, 6)  # Show 6 projects per page
    page = request.GET.get('page')
    
    try:
        projects_page = paginator.page(page)
    except PageNotAnInteger:
        projects_page = paginator.page(1)
    except EmptyPage:
        projects_page = paginator.page(paginator.num_pages)
    
    context = {
        'projects': projects_page,
        'category_filter': category_filter,
        'company_info': {
            'name': 'Elite Construction',
            'phone': '+1-555-0123',
        }
    }
    
    return render(request, 'core/portfolio.html', context)


