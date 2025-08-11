from rest_framework import serializers
from .models import Certificate
import base64

class CertificateSerializer(serializers.ModelSerializer):
    certificate_base64 = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = '__all__'

    def get_certificate_base64(self, obj):
        if obj.certificate_file:
            with obj.certificate_file.open('rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')
        return None
