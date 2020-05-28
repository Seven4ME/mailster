from rest_framework import serializers
from email_import.models import Sending

class EmailOpenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sending
        fields = '__all__'