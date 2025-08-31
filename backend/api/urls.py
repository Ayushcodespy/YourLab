from django.urls import path
from .views import (
    RegisterView, 
    AppointmentCreateView, 
    DoctorAppointmentsView, 
    PatientAppointmentsView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("appointments/create/", AppointmentCreateView.as_view(), name="appointment_create"),
    path("appointments/doctor/", DoctorAppointmentsView.as_view(), name="doctor_appointments"),
    path("appointments/patient/", PatientAppointmentsView.as_view(), name="patient_appointments"),
]
