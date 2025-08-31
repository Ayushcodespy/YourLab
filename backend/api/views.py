from rest_framework import generics, permissions
from .serializers import AppointmentSerializer
from .models import Appointments

# ✅ Patient creates an appointment
class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set logged-in user as patient
        serializer.save(patient=self.request.user)


# ✅ Doctor views their appointments
class DoctorAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only appointments for logged-in doctor
        return Appointments.objects.filter(doctor=self.request.user)


# ✅ Patient views their own appointment history
class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only appointments for logged-in patient
        return Appointments.objects.filter(patient=self.request.user)
