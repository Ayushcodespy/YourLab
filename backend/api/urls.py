from django.urls import path
from .views import (
    AppointmentCreateView,
    DoctorAppointmentListView,
    PatientAppointmentListView
)

urlpatterns = [
    # Patient books appointment
    path("appointments/create/", AppointmentCreateView.as_view(), name="appointment_create"),

    # Doctor sees own appointments
    path("appointments/doctor/", DoctorAppointmentListView.as_view(), name="doctor_appointments"),

    # Patient sees own appointment history
    path("appointments/patient/", PatientAppointmentListView.as_view(), name="patient_appointments"),
]
