from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import (
    HeroSection, FeaturedProject, Model3D, AboutSection, Education,
    SkillCategory, Experience, WorkExperience, Achievement,
    ContactInfo, ResumeSection, SiteSettings
)

def portfolio_view(request):
    # Get all the data from the database
    context = {
        'hero_section': HeroSection.objects.filter(is_active=True).first(),
        'featured_projects': FeaturedProject.objects.filter(is_active=True),
        'models_3d': Model3D.objects.filter(is_active=True),
        'about_section': AboutSection.objects.filter(is_active=True).first(),
        'education': Education.objects.filter(is_active=True),
        'skill_categories': SkillCategory.objects.filter(is_active=True).prefetch_related('skills'),
        'experiences': Experience.objects.filter(is_active=True),
        'work_experiences': WorkExperience.objects.filter(is_active=True),
        'achievements': Achievement.objects.filter(is_active=True),
        'resume_section': ResumeSection.objects.filter(is_active=True).first(),
        'contact_info': ContactInfo.objects.filter(is_active=True).first(),
        'site_settings': SiteSettings.objects.first(),
    }
    
    return render(request, 'index.html', context)

@csrf_exempt
@require_POST
def contact_form_view(request):
    try:
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Validate required fields
        if not all([name, email, subject, message]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            }, status=400)
        
        # Create email content
        email_subject = f"Portfolio Contact: {subject}"
        email_message = f"""
Hello Marcelo,

You have received a new message from your portfolio website:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
This message was sent from your portfolio contact form.
Reply directly to: {email}
        """
        
        # Send email
        try:
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['marceloa.salinas2@gmail.com'],
                reply_to=[email],
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Your message has been sent successfully! I\'ll get back to you soon.'
            })
            
        except Exception as e:
            print(f"Email sending error: {e}")
            return JsonResponse({
                'success': False,
                'message': 'Failed to send message. Please try again or email me directly at marceloa.salinas2@gmail.com'
            }, status=500)
            
    except Exception as e:
        print(f"Contact form error: {e}")
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again.'
        }, status=500)
