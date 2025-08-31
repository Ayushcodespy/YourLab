
from django.conf import settings
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



def doctor_image_path(instance, filename):
    return f"doctorsimage/doctor_{instance.id}/{filename}"

def patient_image_path(instance, filename):
    return f"patientsimage/patient_{instance.id}/{filename}"

# Doctors Profile Model
class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to=doctor_image_path, null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.user.full_name}"


# Patients Profile Model
class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField()
    medical_history = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to=patient_image_path, blank=True, null=True)

    def __str__(self):
        return f"{self.user.full_name} (Patient)"
    

# Appointments Model
class Appointments(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    )

    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_appointments",
        limit_choices_to={"role": "doctor"}   # sirf doctors hi select ho
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_appointments",
        limit_choices_to={"role": "patient"}  # sirf patients hi select ho
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment: {self.patient.full_name} with Dr. {self.doctor.full_name} on {self.appointment_date}"
