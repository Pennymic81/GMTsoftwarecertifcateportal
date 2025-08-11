from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/api/certificates/')),  # Add this line
    path('admin/', admin.site.urls),
    path('api/', include('certificates.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
