# api/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'role']


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['specialization', 'license_no', 'age', 'gender', 'medical_history']


# Registration Serializer (Doctor / Patient)
class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'role', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        password = validated_data.pop('password')

        # Create User
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Create Profile if provided
        if profile_data:
            Profile.objects.create(user=user, **profile_data)

        return user
