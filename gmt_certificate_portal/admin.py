from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'certificate_number', 'course_of_study', 'year_of_graduation')
    search_fields = ('name', 'certificate_number', 'course_of_study')
