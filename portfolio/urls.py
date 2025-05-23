"""Portfolio URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from main import views

def health_check(request):
    """Simple health check endpoint for Railway"""
    return JsonResponse({'status': 'healthy', 'app': 'portfolio'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health'),
    path('', views.portfolio_view, name='index'),
    path('contact/', views.contact_form_view, name='contact'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 