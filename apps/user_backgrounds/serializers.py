from .models import UserBackground
from rest_framework import serializers


class UserBackgroundSerializer(serializers.ModelSerializer):
    background_id = serializers.CharField(required=True)
    company_logo = serializers.ImageField(required=True)
    company_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    role = serializers.CharField(required=True)

    class Meta:
        model = UserBackground
        fields = '__all__'

