from rest_framework import serializers
from .models import OTPcontact


class verify_serializers(serializers.ModelSerializer):
    class Meta:
        model = OTPcontact
        fields = ['Contact', 'OTP','Name', 'Email']

