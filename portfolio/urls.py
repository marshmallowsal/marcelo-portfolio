"""Portfolio URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from main import views

@csrf_exempt
@never_cache
def health_check(request):
    """Simple health check endpoint for Railway"""
    return HttpResponse("OK", content_type="text/plain", status=200)

@csrf_exempt
@never_cache
def simple_test(request):
    """Ultra simple test endpoint"""
    return HttpResponse("WORKING", content_type="text/plain", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health'),
    path('healthcheck/', health_check, name='healthcheck'),
    path('test/', simple_test, name='test'),
    path('', views.portfolio_view, name='index'),
    path('contact/', views.contact_form_view, name='contact'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 