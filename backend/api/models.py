# api/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name", "role"]

    def __str__(self):
        return f"{self.full_name} ({self.role})"


# Profile Model (extra details)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # Doctor specific fields
    specialization = models.CharField(max_length=255, blank=True, null=True)
    license_no = models.CharField(max_length=100, blank=True, null=True)

    # Patient specific fields
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.full_name}"
