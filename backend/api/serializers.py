from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import DoctorProfile, PatientProfile, Appointments

User = get_user_model()

# ------------------- REGISTER SERIALIZER -------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})  # confirm password

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'role', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # remove confirm password
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Automatically create profile based on role
        from .models import DoctorProfile, PatientProfile
        if user.role == 'doctor':
            DoctorProfile.objects.create(user=user)
        elif user.role == 'patient':
            PatientProfile.objects.create(user=user)

        return user


# ------------------- USER SERIALIZER -------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name", "email", "role", "username"]


# ------------------- DOCTOR PROFILE SERIALIZER -------------------
class DoctorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested user details

    class Meta:
        model = DoctorProfile
        fields = ["id", "user", "specialization", "phone", "profile_image"]


# ------------------- PATIENT PROFILE SERIALIZER -------------------
class PatientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PatientProfile
        fields = ["id", "user", "age", "medical_history", "phone", "profile_image"]


# ------------------- APPOINTMENT SERIALIZER -------------------
class AppointmentSerializer(serializers.ModelSerializer):
    doctor = UserSerializer(read_only=True)   # Read-only nested doctor info
    patient = UserSerializer(read_only=True)  # Read-only nested patient info

    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role="doctor"),
        source="doctor",
        write_only=True
    )

    class Meta:
        model = Appointments
        fields = [
            "id", "doctor", "patient", "doctor_id",
            "appointment_date", "appointment_time",
            "reason", "status", "created_at"
        ]